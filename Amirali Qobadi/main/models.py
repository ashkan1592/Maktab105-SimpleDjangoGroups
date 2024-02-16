from django.db import models


# Create your models here.

class Urls(models.Model):
    url = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255,null=True)
