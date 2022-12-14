from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import SurvivorsSerializer,AddressSerializer
from .models import Survivors,Address

class ListsurvivorsAPIView(ListAPIView):
    """This endpoint list all of the available survivors from the database"""
    serializer_class = SurvivorsSerializer
    queryset = Survivors.objects.all()

class CreateSurvivorsAPIView(CreateAPIView):
    """This endpoint allows for creation of a survivors"""
    serializer_class = SurvivorsSerializer
    queryset = Survivors.objects.all()

class CreateAddressAPIView(CreateAPIView):
    """This endpoint allows for creation of a address for survivors"""
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class UpdateSurvivorAddressAPIViews(UpdateAPIView):
    """This endpoint allows for updating a specific survivors Address by passing in the id of the survivors to update"""
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class UpdateSurvivorAPIViews(UpdateAPIView):
    """This endpoint allows for updating a specific survivors Address by passing in the id of the survivors to update"""
    serializer_class = SurvivorsSerializer
    queryset = Survivors.objects.all()