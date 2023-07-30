from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, MenuPatchSerializer, BookingSerializer

# Create your views here!
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self, request):
        user = self.request.user
        serial_data = self.get_serializer(data=request.data)
        serial_data.is_valid(raise_exception=True)
        title = serial_data.validated_data['title']
        price = serial_data.validated_data['price']
        inventory = serial_data.validated_data['inventory']

        menu_item = Menu.objects.filter(title__iexact=title)
        if menu_item:
            return Response({"message": "Menu item exists"}, status=status.HTTP_400_BAD_REQUEST)

        new_menu_item = Menu(title=title, price=price, inventory=inventory)
        new_menu_item.save()
        return Response(model_to_dict(new_menu_item))

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return MenuPatchSerializer
        else:
            return MenuSerializer
    
    def put(self, request, pk):
        user = self.request.user
        serial_data = self.get_serializer(data=request.data)
        serial_data.is_valid(raise_exception=True)

        try:
            menu_item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response({"message": "Menu item not found"}, status=status.HTTP_400_BAD_REQUEST)

        serial_data = self.get_serializer(menu_item, data=request.data, partial=False)
        if serial_data.is_valid(raise_exception=True):
            serial_data.save()
            return Response(serial_data.data)
        return Response(serial_data.errors)
    
    def patch(self, request, pk):
        user = self.request.user
        serial_data = self.get_serializer(data=request.data)
        serial_data.is_valid(raise_exception=True)

        try:
            menu_item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response({"message": "Menu item not found"}, status=status.HTTP_400_BAD_REQUEST)

        serial_data = self.get_serializer(menu_item, data=request.data, partial=True)
        if serial_data.is_valid(raise_exception=True):
            serial_data.save()
            return Response(serial_data.data)
        return Response(serial_data.errors)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
