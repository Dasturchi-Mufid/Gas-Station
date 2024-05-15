from rest_framework.serializers import ModelSerializer
from main import models

class GasStationSerializer(ModelSerializer):
    class Meta:
        model = models.GasStation
        fields = '__all__'



class GasTypeSerializer(ModelSerializer):
    class Meta:
        model = models.GasType
        fields = '__all__'


class StationImageSerializer(ModelSerializer):
    class Meta:
        model = models.StationImage
        fields = '__all__'