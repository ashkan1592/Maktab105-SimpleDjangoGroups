from django.db import models


# Create your models here.

# class Song(models.Model):
#     name = models.CharField(max_length=100)
#     cover = models.CharField(max_length=200)
#     url = models.CharField(max_length=200)
#     category = models.CharField(max_length=110)


##
class Category(models.Model):
    category = models.CharField(max_length=100)


class Song(models.Model):
    name = models.CharField(max_length=100)
    cover = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='songs')
