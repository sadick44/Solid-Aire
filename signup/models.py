from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    discount = models.FloatField()


class Registration(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    image_url = models.CharField(max_length=2020)