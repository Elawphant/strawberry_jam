
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import Shelf

@strawberry_django.order(Shelf)
class ShelfOrder:
    id: auto
    books: auto

    id: auto

    number: auto

