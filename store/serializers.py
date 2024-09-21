from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GroceryItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = ['id', 'name', 'quantity', 'created_at', 'updated_at']