from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GroceryItemSerializer
from store.utils import generate_category
from store.models import GroceryItem
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication

class IndexView(CreateAPIView):
    serializer_class = GroceryItemSerializer
    queryset = GroceryItem.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    

class UpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroceryItemSerializer
    queryset = GroceryItem.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



