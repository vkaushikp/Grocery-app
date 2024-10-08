from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', IndexView.as_view(), name='api-index'),
    path('items/<int:pk>/', UpdateView.as_view(), name='item-update'),
    path('login/', 
         jwt_views.TokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
    path('token/refresh/', 
         jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'),
]
