from .base import BaseModel
from django.db import models


class Request(BaseModel):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    content_type = models.CharField(max_length=1000)
    user_agent= models.CharField(max_length=2500)
