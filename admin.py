
from django.contrib import admin
from .models import Survivors,Address

@admin.register(Survivors)
class SurvivorsAdmin(admin.ModelAdmin):
    fields = ['name','age', 'gender']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ['latitude','longitude']
