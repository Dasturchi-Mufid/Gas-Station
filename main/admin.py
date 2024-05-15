from django.contrib import admin
from . import models
admin.site.register(models.GasStation)
admin.site.register(models.GasType)
admin.site.register(models.StationImage)