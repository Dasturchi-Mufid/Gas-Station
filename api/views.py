from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from main import models
from . import serializers
from . import permission

@api_view(['GET'])
def gas_type_list(request):
    gas_types = models.GasType.objects.all()
    serializer = serializers.GasTypeSerializer(gas_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gas_type_create(request):
    serializer = serializers.GasTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def gas_type_detail(request, pk):
    gas_type = get_object_or_404(models.GasType, id=pk)
    serializer = serializers.GasTypeSerializer(gas_type)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def gas_type_update(request, pk):
    gas_type = get_object_or_404(models.GasType, id=pk)
    station = gas_type.station

    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    partial = request.method == 'PATCH'
    serializer = serializers.GasTypeSerializer(gas_type, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def gas_type_delete(request, pk):
    gas_type = get_object_or_404(models.GasType, id=pk)
    station = gas_type.station

    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    gas_type.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def station_image_list(request):
    station_images = models.StationImage.objects.all()
    serializer = serializers.StationImageSerializer(station_images, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def station_image_create(request):
    serializer = serializers.StationImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def station_image_detail(request, pk):
    station_image = get_object_or_404(models.StationImage, id=pk)
    serializer = serializers.StationImageSerializer(station_image)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated, permission.OwnerPermission])
def station_image_update(request, pk):
    station_image = get_object_or_404(models.StationImage, id=pk)
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
def station_image_delete(request, pk):
    station_image = get_object_or_404(models.StationImage, id=pk)
    station = station_image.station

    if not permission.OwnerPermission().has_object_permission(request, None, station):
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    station_image.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def station_images_for_station(request, station_id):
    station = get_object_or_404(models.GasStation, id=station_id)
    station_images = models.StationImage.objects.filter(station=station)
    serializer = serializers.StationImageSerializer(station_images, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def gas_types_for_station(request, station_id):
    station = get_object_or_404(models.GasStation, id=station_id)
    gas_types = models.GasType.objects.filter(station=station)
    serializer = serializers.GasTypeSerializer(gas_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
