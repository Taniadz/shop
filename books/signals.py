from books.models import Book
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import logging


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Book)
def save_book(instance, **kwargs):
    if kwargs['created']:
        logger.info("New book was created: ")
    else:
        logger.info("Book was edited: ")
    logger.info(Book.objects.filter(id=instance.id).values()[0])


@receiver(post_delete, sender=Book)
def delete_book(instance, **kwargs):
    logger.info("Book was deleted: ")
    logger.info('%s %s Price: %s' % (instance.title, instance.ISBN, instance.price))

