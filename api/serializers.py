from api.models import Shoe, ShoeColor, ShoeType, Manufacturer
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField

class ShoeSerializer(ModelSerializer):
    manufacturer = StringRelatedField()
    color = StringRelatedField()
    shoe_type = StringRelatedField()
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        )


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name',)
 

class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')
