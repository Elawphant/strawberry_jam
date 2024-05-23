
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import BookInfo

@strawberry_django.filter(BookInfo, lookups=True)
class BookInfoFilter:
    id: auto
    book: auto
    title: auto
    subtitle: auto
    pages: auto
    is_novel: auto
    publication_date: auto
