from django.db import models


# Create your models here.

class Add(models.Model):
    name = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
