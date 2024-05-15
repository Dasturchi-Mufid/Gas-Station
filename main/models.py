from django.db import models
from django.contrib.auth.models import User


class GasStation(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StationImage(models.Model):
    image = models.ImageField(upload_to='station_images')
    station = models.ForeignKey(GasStation,on_delete=models.CASCADE)

    def __str__(self):
        return self.station.name



class GasType(models.Model):
    name = models.CharField(max_length=200)
    station = models.ForeignKey(GasStation,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_have = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.station.name}'