from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from main import models
from . import serializers
from . import permission

@api_view(['GET'])
def station_list(request):
    station_list = models.GasStation.objects.all()
    serializer = serializers.GasStationSerializer(station_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def station_create(request):
    serializer = serializers.GasStationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def station_detail(request, code):
    try:
        station = models.GasStation.objects.get(code=code)
    except models.GasStation.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.GasStationSerializer(station)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def station_update(request, code):
    try:
        station = models.GasStation.objects.get(code=code)
    except models.GasStation.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
    partial = request.method == 'PATCH'
    serializer = serializers.GasStationSerializer(station, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def station_delete(request, code):
    try:
        station = models.GasStation.objects.get(code=code)
    except models.GasStation.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
    station.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def station_search(request):
    query = request.query_params.get('q', None)
    if query is not None:
        stations = models.GasStation.objects.filter(name__icontains=query)
        serializer = serializers.GasStationSerializer(stations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"detail": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def gas_type_list(request):
    gas_types = models.GasType.objects.all()
    serializer = serializers.GasTypeSerializer(gas_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def station_image_create(request):
    serializer = serializers.StationImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def station_image_update(request, code):
    station_image = get_object_or_404(models.StationImage, code=code)
    station = station_image.station

    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    partial = request.method == 'PATCH'
    serializer = serializers.StationImageSerializer(station_image, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def station_image_delete(request, code):
    station_image = get_object_or_404(models.StationImage, code=code)
    station = station_image.station

    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    station_image.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def station_images_for_station(request, station_code):
    station = get_object_or_404(models.GasStation, code=station_code)
    station_images = models.StationImage.objects.filter(station=station)
    serializer = serializers.StationImageSerializer(station_images, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def gas_types_for_station(request, station_code):
    station = get_object_or_404(models.GasStation, code=station_code)
    gas_types = models.GasType.objects.filter(station=station)
    serializer = serializers.GasTypeSerializer(gas_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
