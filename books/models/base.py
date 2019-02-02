from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    created = models.DateTimeField(default=datetime.now, blank=True)
    changed = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
