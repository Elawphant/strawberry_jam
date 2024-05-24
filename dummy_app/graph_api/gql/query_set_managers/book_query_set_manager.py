
from strawberry_jam.queryset import QuerySetManager
from library.models import Book


class BookQuerySetManager(QuerySetManager):
    model = Book

    # implement your custom queryset here by overwriting def get_queryset
