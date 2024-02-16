from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    cover = models.CharField(max_length=20)
    category = models.CharField(max_length=20)