from rest_framework import permissions, status, generics
from rest_framework.response import Response
from django_filters import rest_framework as filters

from fornex.account_app.serializers import ListAccountSerializer, RegisterAccountSerializer
from fornex.account_app.models import Account


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = ListAccountSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('is_verified','username' )

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        elif self.request.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def post(self, request, *args, **kwargs):
        serializer = RegisterAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = ListAccountSerializer
    permission_classes = [permissions.IsAdminUser]
