
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated

from library.models import Author

@strawberry_django.filter(Author, lookups=True)
class ('AuthorFilter',):
    id: auto
    id: auto

    name: auto

    authors_connection: auto

