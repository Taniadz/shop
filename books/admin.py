from django.contrib.admin import register
from django.contrib.admin import ModelAdmin
from books import models


@register(models.Book)
class ResourceBaseAdmin(ModelAdmin):
    pass


@register(models.Author)
class AuthorAdmin(ModelAdmin):
    pass
