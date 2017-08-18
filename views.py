from django.shortcuts import render
from rest_framework import viewsets
from .Serializers import CustomerSerializer
from .Serializers import AddressSerializer
from .models import Customer
from .models import Address
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
