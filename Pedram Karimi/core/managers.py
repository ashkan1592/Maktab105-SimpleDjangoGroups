from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        """
        Soft delete objects in the queryset.

        Instead of permanently deleting objects from the database,
        mark them as deleted by setting the 'is_deleted' field to True.
        """
        return super().update(is_deleted=True)


class ActiveObjectsManager(models.Manager):
    def get_queryset_object(self):
        """
        Get the queryset object associated with this manager.

        If the queryset object has not been created yet, create it
        using ManagerQuerySetDelete to handle soft deletion.
        """
        if not hasattr(self.__class__, '__queryset'):
            self.__class__.__queryset = SoftDeleteQuerySet(self.model)
        return self.__queryset

    def get_queryset(self):
        """
        Get the filtered queryset, excluding deleted and inactive objects.

        This method filters out objects marked as deleted ('is_deleted'=True)
        and inactive ('is_active'=False) from the queryset.
        """
        return self.get_queryset_object().filter(is_active=True, is_deleted=False)

    def archive(self):
        """
        Retrieve all objects, including deleted and inactive ones.

        This method returns all objects in the queryset, including those
        marked as deleted or inactive. It is provided as an alias for
        get_queryset() but may be redundant in most use cases.
        """
        return super().get_queryset()


class ActivatableFalseMixin(models.Model):
    """
    Mixin to add activation functionality to models.
    """
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ActiveStatusTrueMixin(models.Model):
    """
    Mixin to add active status functionality to models.
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SoftDeletableFalseMixin(models.Model):
    """
    Mixin to add soft deletion functionality to models.
    """
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class LogicalStatusMixin(ActiveStatusTrueMixin, SoftDeletableFalseMixin):
    """
    Mixin to add logical status fields for products.
    """
    objects = ActiveObjectsManager()

    class Meta:
        abstract = True
