from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from fornex.account_app.models import Account


class ListAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for Account model.

    This serializer provides all fields of the Account model and includes
    validation for updating certain fields:
    - The 'username' field cannot be changed once set.
    - The 'balance' field can only be updated if the user is verified.
    """

    class Meta:
        model = Account
        fields = '__all__'
    
    def update(self, instance, validated_data):
        # Check if 'username' is being changed
        current_username = instance.username
        new_username = validated_data.get('username')
        if new_username and current_username != new_username:
            raise serializers.ValidationError('Username cannot be changed')
        
        # Check if 'balance' is being changed by an unverified user
        user_is_verified = instance.is_verified
        current_balance = instance.balance
        new_balance = validated_data.get('balance')
        if not user_is_verified and new_balance and current_balance != new_balance:
            raise serializers.ValidationError('User is not verified. It is impossible to change the balance.')

        return super().update(instance, validated_data)


class RegisterAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Account.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user