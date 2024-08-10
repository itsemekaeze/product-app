from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=1024)
