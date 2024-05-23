
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import BookInfo

@strawberry_django.order(BookInfo)
class BookInfoOrder:
    id: auto
    id: auto

    book: auto

    title: auto

    subtitle: auto

    pages: auto

    is_novel: auto

    publication_date: auto

