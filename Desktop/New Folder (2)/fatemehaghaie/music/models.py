from django.db import models
class Music(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    url=models.URLField(max_length=100)
    cover=models.URLField(max_length=100)
    def __str__(self):
        return self.name
