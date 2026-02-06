from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import authentication, permissions

from grocery_management.serializers import UserSerializer, GrocerySerializer
from grocery_management.models import Grocery
from grocery_management.permissions import IsOwner


class UserSignupView(CreateAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer


class GroceryCreateListView(CreateAPIView, ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = GrocerySerializer

    def get_queryset(self):
        return Grocery.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    

class GroceryRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    serializer_class = GrocerySerializer

    def get_queryset(self):
        return Grocery.objects.all()
    



