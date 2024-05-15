from django.db import models
from django.contrib.auth.models import User
from random import sample
import string



class CodeGenerate(models.Model):
    code = models.CharField(max_length=255, blank=True, unique=True)
    
    @staticmethod
    def generate_code():
        return ''.join(sample(string.ascii_letters + string.digits, 15)) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                code = self.generate_code()
                if not self.__class__.objects.filter(code=code).count():
                    self.code = code
                    break
        super(CodeGenerate,self).save(*args, **kwargs)

    class Meta:
        abstract = True


class GasStation(CodeGenerate):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StationImage(CodeGenerate):
    image = models.ImageField(upload_to='station_images')
    station = models.ForeignKey(GasStation,on_delete=models.CASCADE)

    def __str__(self):
        return self.station.name



class GasType(CodeGenerate):
    name = models.CharField(max_length=200)
    station = models.ForeignKey(GasStation,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_have = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.station.name}'