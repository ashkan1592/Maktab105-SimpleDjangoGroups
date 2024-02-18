from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    cover = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
