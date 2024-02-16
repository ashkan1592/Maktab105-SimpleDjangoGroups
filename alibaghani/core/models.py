from django.db import models


class DateTimeField(models.Model):
    creat_time = models.DateField(auto_now_add=True, editable=False)
    update_time = models.DateField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-update_time']


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, auto_created=True)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True
        ordering = ['-name']
