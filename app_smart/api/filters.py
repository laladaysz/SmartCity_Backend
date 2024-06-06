import django_filters
from app_smart.models import ContadorData, LuminosidadeData, Sensor, TemperaturaData, UmidadeData
from .serializers import SensorSerializer, TemperaturaDataSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

# Definindo filtros GET
class SensorFilter(django_filters.FilterSet):
  # Criamos os campos que terão filtragem
  responsavel = django_filters.CharFilter(field_name='responsavel', # Nome do campo 
                                          lookup_expr='icontains') # Mostrar qualquer resultado que conter a pesquisa (maius, minus etc.)
  
  status_operacional = django_filters.CharFilter(field_name='status_operacional',lookup_expr='exact')
  tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='exact')
  localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='icontains')

  class Meta:
    model = Sensor
    fields = ['responsavel', 'status_operacional', 'tipo', 'localizacao']

# Define os filtros POST
class TemperaturaFilterView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, *args, **kwargs):
    sensor_id = request.data.get('sensor_id', None)
    # Maior e menor que 
    valor_gte = request.data.get('valor_gte', None)
    valor_lt = request.data.get('valor_lt', None)

    timestamp_gte = request.data.get('timestamp_gte', None)
    timestamp_lt = request.data.get('timestamp_lt', None)

    filters = Q()

    if sensor_id:
      filters &= Q(sensor_id = sensor_id)
    if valor_gte:
      filters &= Q(valor_gte = valor_gte)
    if valor_lt:
      filters &= Q(valor_lt = valor_lt)
    if timestamp_gte:
      filters &= Q(timestamp_gte = timestamp_gte)
    if timestamp_lt:
      filters &= Q(timestamp_lt = timestamp_lt)
    
    queryset = TemperaturaData.objects.filter(filters)
    serializer = TemperaturaDataSerializer(queryset, many=True)
    return Response(serializer.data)

# Definindo filtros GET
class TemperaturaDataFilter(django_filters.FilterSet):
  timestamp_gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
  timestamp_lte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')
  
  sensor = django_filters.DateTimeFilter(field_name='sensor')

  valor_gte = django_filters.DateTimeFilter(field_name='valor', lookup_expr='gte')
  valor_lte = django_filters.DateTimeFilter(field_name='valor', lookup_expr='lte')

  class Meta: 
    model = TemperaturaData
    fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte']

# Definindo filtros post
class SensorFilterView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, *args, **kwargs):
    # Definindo argumentos para serem passados
    tipo = request.data.get('tipo', None)
    localizacao = request.data.get('localizacao', None)
    responsavel = request.data.get('responsavel', None)
    status_operacional = request.data.get('status_operacional', None)

    # Transforma as pesquisas do python para uma query SQL (comandos)
    filters = Q()

    if tipo:
      filters &= Q(tipo__icontains=tipo)
    if localizacao:
      filters &= Q(localizacao__icontains=localizacao)
    if responsavel:
      filters &= Q(responsavel__icontains=responsavel)
    if status_operacional:
      filters &= Q(status_operacional=status_operacional)
    

    queryset = Sensor.objects.filter(filters)
    serializer = SensorSerializer(queryset, many=True)
    return Response(serializer.data)
    
    # No tipo GET deixa exposto na URL
    # No caso de filter POST é passado num JSON
    

class UmidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp.lt', None)
        
        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
            
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
            
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
            
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
            
        queryset = UmidadeData.objects.filter(filters) 
        serializer = serializer.UmidadeDataserializer(queryset, many = True)
        return Response(serializer.data)           
            
            
class LuminosidadeFilterView(APIView):
    Permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)
        filters = Q() # Inicializa um filtro vazio
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
        queryset = LuminosidadeData.objects.filter(filters)
        serializer = serializer.LuminosidadeDataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class ContadorFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)
        filters = Q() # Inicializa um filtro vazio
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
        queryset = ContadorData.objects.filter(filters)
        count = queryset.count()
        serializer = serializer.ContadorDataSerializer(queryset, many=True)
        response_data = {
        'count': count,
        'results': serializer.data
        }
        return Response(response_data)