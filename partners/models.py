from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    class Meta:
        app_label = 'partners'
        db_table = 'customer'


class Manufacturer(models.Model):
    title = models.CharField(max_length=256)
    manager = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)

    class Meta:
        app_label = 'partners'
        db_table = 'manufacturer'
