from rest_framework import serializers
from . models import Customer
from . models import Address
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['mobile_no', 'phone_no', 'email_id', 'first_name', 'last_name', 'age','Addresses']
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'