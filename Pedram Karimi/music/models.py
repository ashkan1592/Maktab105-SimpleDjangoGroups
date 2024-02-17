from django.db import models
# from core.managers import LogicalStatusProductMixin
from core.models import TimestampedModel, BaseModel


class AlbumModel(TimestampedModel, BaseModel):
    """
    Model representing an album.

    Inherits:
        TimestampedModel: Provides timestamp fields for creation and update times.
        BaseModel: Provides a base model with common fields like ID and name.
        ActivatableFalseMixin: Provides a boolean field is_active set to False.
    """
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='Album',
                                 verbose_name='categories')


class CategoryModel(TimestampedModel, BaseModel):
    """
    Model representing a category.

    Inherits:
        TimestampedModel: Provides timestamp fields for creation and update times.
        BaseModel: Provides a base model with common fields like ID and name.
        ActivatableFalseMixin: Provides a boolean field is_active set to False.
    """
    pass


class MusicModel(TimestampedModel, BaseModel):
    """
    Model representing a music item.

    Attributes:
        url (URLField): The URL of the music.
        cover (ImageField): The image cover of the music.
        album (ForeignKey): The album to which the music belongs.

    Inherits:
        TimestampedModel: Provides timestamp fields for creation and update times.
        BaseModel: Provides a base model with common fields like ID and name.
        ActivatableFalseMixin: Provides a boolean field is_active set to False.
    """
    url = models.URLField(max_length=100, unique=True, null=True)
    cover = models.ImageField(upload_to='media', null=True)
    album = models.ForeignKey(AlbumModel, on_delete=models.CASCADE, related_name='musics', verbose_name='albums')


'''
    +-------------+          +---------------+          +------------+
    |   Category  |          |     Album     |          |   Music    |
    +-------------+          +---------------+          +------------+
    |    - id     |          |      - id     |          |    - id    |
    |created_at   |          |created_at     |          |    url     |
    |updated_at   |          |updated_at     |          |   cover    |
    | is_active   |          | is_active     |          |  album_id  |
    | is_deleted  |          | is_deleted    |          |created_at  |
    +-------------+          +---------------+          |updated_at  |
                                                        | is_active  |
                                                        | is_deleted |
                                                        +------------+

'''
