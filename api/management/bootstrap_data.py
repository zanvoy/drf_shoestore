from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeColor, ShoeType

class Command(BaseCommand):
    COLOR_CHOICES= [
        'Red',
        'Orange', 
        'Yellow', 
        'Green',
        'Blue', 
        'Indigo',
        'Violet', 
        'Black',
        'White'
    ]
    TYPE_CHOICES = [
        'sneaker',
        'boot',
        'sandal',
        'dress',
        'other',
    ]
    def handle(self, ShoeColor, ShoeType):
        for item in COLOR_CHOICES:
            ShoeColor.objects.create(color_name=item)
        for item in TYPE_CHOICES:
            ShoeType.objects.create(style=item)