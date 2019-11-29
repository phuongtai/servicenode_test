from rest_framework import serializers
from .models import Manufacturer, Customer


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=256)
    phone = serializers.CharField(max_length=256)
    address = serializers.CharField(max_length=256)

    class Meta:
        model = Customer
        fields = '__all__'


class ReprCustomerSerializer(serializers.ModelSerializer):
    partner = serializers.CharField(source='name')
    contact = serializers.CharField(source='phone')

    class Meta:
        model = Customer
        fields = ('partner', 'contact')


class ManufacturerSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256)
    manager = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ReprManufacturerSerializer(serializers.ModelSerializer):
    partner = serializers.CharField(source='title')
    contact = serializers.CharField(source='owner')

    class Meta:
        model = Manufacturer
        fields = ('partner', 'contact')
