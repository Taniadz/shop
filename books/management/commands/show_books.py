from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('order', nargs='?', default="desc", type=str,
                            help='Argument for ordering books by publish_date')

    def handle(self, *args, **options):
        sort_key = options.get("order")

        if sort_key == "desc":
            books = Book.objects.order_by("-publish_date")[:10]
        else:
            books = Book.objects.order_by("publish_date")[:10]

        self.stdout.write(self.style.SUCCESS(books))
