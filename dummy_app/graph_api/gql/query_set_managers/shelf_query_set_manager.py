
from strawberry_jam.queryset import QuerySetManager
from library.models import Shelf


class ShelfQuerySetManager(QuerySetManager):
    model = Shelf

    # implement your custom queryset here by overwriting def get_queryset
