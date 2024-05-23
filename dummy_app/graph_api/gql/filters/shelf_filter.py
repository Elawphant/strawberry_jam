
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import Shelf

@strawberry_django.filter(Shelf, lookups=True)
class ShelfFilter:
    books: auto
    id: auto
    number: auto
