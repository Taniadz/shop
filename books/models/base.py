from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(default=timezone.now, blank=True)
    changed = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
