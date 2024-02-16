from django.db import models


# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    url = models.URLField()
    cover = models.URLField()

    def __str__(self):
        return self.name
