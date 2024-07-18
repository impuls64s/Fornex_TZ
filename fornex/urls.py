from django.urls import include, path
from rest_framework import routers

from fornex.account_app import views

router = routers.DefaultRouter()
# router.register(r'users', views.AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.AccountList.as_view()),
    path('users/<int:pk>/', views.AccountDetail.as_view()),
]