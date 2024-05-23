
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import Book

@strawberry_django.order(Book)
class BookOrder:
    id: auto
    books_connection: auto

    bookinfo: auto

    id: auto

    books_connection: auto

