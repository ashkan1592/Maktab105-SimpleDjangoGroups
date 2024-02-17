from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Add(models.Model):
    name = models.CharField(max_length=200)
    cover=models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
         return self.name