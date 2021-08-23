from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Car(models.Model):
    name=models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    manufacturer=models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


