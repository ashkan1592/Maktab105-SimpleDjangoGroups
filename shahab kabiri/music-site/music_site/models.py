from django.db import models

class Musics(models.Model):
    name = models.CharField(max_length=105)
    cover=models.TextField()
    category=models.CharField(max_length=150)
    url=models.URLField()
