from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False
    )

    class Meta:
        abstract = True


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserTrackedModel(models.Model):
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    deleted_by = models.IntegerField(default=0)

    class Meta:
        abstract = True