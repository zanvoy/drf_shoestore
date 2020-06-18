from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import ShoeColorSerializer, ShoeSerializer, ManufacturerSerializer, ShoeTypeSerializer
from api.models import Shoe, ShoeColor, ShoeType, Manufacturer

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    queryset = Shoe.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'shoe color'
    queryset = ShoeColor.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'shoe type'
    queryset = ShoeType.objects.all()

class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()