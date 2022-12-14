from rest_framework import serializers
from .models import Survivors,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','latitude','longitude','survivors']

class SurvivorsSerializer(serializers.ModelSerializer):
    
    location = AddressSerializer(many=True,read_only=True)
    class Meta:
        model = Survivors
        fields = ['id','name','age','gender','location']
       



        