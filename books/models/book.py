from django.db import models
from .base import BaseModel
from django.urls import reverse
from django.utils import timezone


class Book(BaseModel):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField("Author")
    price = models.FloatField()
    ISBN = models.CharField(max_length=150, unique=True)
    publish_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s Price: %s' % (self.title, self.ISBN, self.price)
