from django.db import models
from .base import BaseModel


class Author(BaseModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

