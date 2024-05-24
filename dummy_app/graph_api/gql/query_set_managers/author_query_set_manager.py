
from strawberry_jam.queryset import QuerySetManager
from library.models import Author


class AuthorQuerySetManager(QuerySetManager):
    model = Author

    # implement your custom queryset here by overwriting def get_queryset
