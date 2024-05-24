
from strawberry_jam.queryset import QuerySetManager
from library.models import BookInfo


class BookInfoQuerySetManager(QuerySetManager):
    model = BookInfo

    # implement your custom queryset here by overwriting def get_queryset
