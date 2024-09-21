from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
    path('create/', GroceryItemCreateView.as_view(), name='create_grc'),
    path('update/<int:pk>/', UpdateGroceryItemView.as_view(), name='update_grc'),
    path('view/<int:pk>/', ViewGroceryItemView.as_view(), name='view_grc'),
    path('delete/<int:pk>/', DeleteGroceryItemView.as_view(), name='delete_grc'),
]
