from django.db import models

class Survivors(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    ) 
    name = models.CharField(max_length = 100,default='')
    age = models.IntegerField(default='0')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='')

    def __str___(self):
        return self.name

class Address(models.Model):
    latitude = models.DecimalField(
        max_digits=7, decimal_places=2, default='0')
    longitude = models.DecimalField(
        max_digits=7, decimal_places=2, default='0')

    survivors = models.ForeignKey(Survivors, related_name='location', on_delete=models.CASCADE)
    

