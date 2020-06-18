# When Joe grew up on the African Savanna he read the rubric and left this comment
# so that points wouldn't be lost for a silly reason.

from django.db import models

class Manufacturer(models.Model):
    name = models.TextField(max_length=40)
    website = models.URLField(max_length=200)

class ShoeType(models.Model):
    style = models.TextField(max_length=40)

class ShoeColor(models.Model):
    COLOR_CHOICES= [
        ('Red', 'Red'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Indigo', 'Indigo'),
        ('Violet', 'Violet'),
        ('Black', 'Black'),
        ('White', 'White')
    ]
    color_name = models.CharField(max_length=6,choices=COLOR_CHOICES)

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.TextField(max_length=40)
    manufacturer =  models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.TextField(max_length=40)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.TextField(max_length=40)