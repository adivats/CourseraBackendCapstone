from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.IntegerField(source='id', read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    inventory = serializers.IntegerField(required=True)

    class Meta:
        model = Menu
        fields = ['menu_item_id', 'title', 'price', 'inventory']

class MenuPatchSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.IntegerField(source='id', read_only=True)
    title = serializers.CharField(required=False, max_length=255)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    inventory = serializers.IntegerField(required=False)

    class Meta:
        model = Menu
        fields = ['menu_item_id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'