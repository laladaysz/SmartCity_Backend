from django.contrib.auth.models import User # type: ignore
from app_smart.api.filters import SensorFilter, TemperaturaDataFilter
from rest_framework import permissions, generics # type: ignore
from app_smart.api import serializers
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from ..models import ContadorData, LuminosidadeData, Sensor, TemperaturaData, UmidadeData
from rest_framework import viewsets # type: ignore
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore


class CreateUserApiViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permissions_classes = [permissions.IsAuthenticated]
    filter_backend = [DjangoFilterBackend]
    filter_class = SensorFilter
    
class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter
    
class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ContadorDataViewSet(viewsets.ModelViewSet):
 queryset = ContadorData.objects.all()
 serializer_class = serializers.ContadorDataSerializer
 permission_classes = [permissions.IsAuthenticated]