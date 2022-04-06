# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Model owner
class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def _unicode_(self):
        return self.name


# Model Building
class Building(models.Model):
    area = models.FloatField()
    number_rooms = models.FloatField()
    price = models.FloatField()
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    town = models.CharField(max_length=50, null=True)

    def _unicode_(self):
        return self.address


# Model Flat
class Flat(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    department_number = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.building.address
