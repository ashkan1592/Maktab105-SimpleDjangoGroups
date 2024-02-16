from django.db import models

from core.models import DateTimeField, BaseModel


class AlbumModel(DateTimeField, BaseModel):
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='Album',
                                 verbose_name='categories')

    def __str__(self):
        return f"{self.id} - {self.name}"


class CategoryModel(DateTimeField, BaseModel):

    def __str__(self):
        return f"{self.id} - {self.name}"


class MusicModel(DateTimeField, BaseModel):
    url = models.URLField(max_length=100, unique=True, null=True)
    cover = models.ImageField(upload_to='media', null=True)
    album = models.ForeignKey(AlbumModel, on_delete=models.CASCADE, related_name='musics', verbose_name='albums')

    def __str__(self):
        return f"{self.id} - {self.name}"
