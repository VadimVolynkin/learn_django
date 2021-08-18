from django.db import models

# ============================================================================
# MANY-TO-ONE: 
# ============================================================================
# В базе будут созданы следующие таблицы:
# manytoone_car
# manytoone_manufacturer


class Car(models.Model):
    name=models.CharField(max_length=255)
    manufacturer=models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""

# ===== QUERIES with MANY TO ONE ===============
# try it in ./manage.py shell

from manytoone.models import Car, Manufacturer

# создать объект производителя
Manufacturer.objects.create(name='audi')

# создать модель авто с привязкой к производителю
m = Manufacturer.objects.get(name='audi')
Car.objects.create(name='a6', manufacturer=m)

# создать модель авто вместе с производителем
Car.objects.create(name='b1', manufacturer=Manufacturer.objects.create(name='bmw'))

# получить все модели авто ауди
audi = Manufacturer.objects.get(name='audi')
audi.car_set.all()
"""

