
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from library.models import BookInfo



@strawberry_django.input(BookInfo, partial=True)
class BookInfoUpdateInput:
    id: strawberry.auto

    book: strawberry.auto = strawberry_django.field()

    title: strawberry.auto = strawberry_django.field()

    subtitle: strawberry.auto = strawberry_django.field()

    pages: strawberry.auto = strawberry_django.field()

    is_novel: strawberry.auto = strawberry_django.field()

    publication_date: strawberry.auto = strawberry_django.field()



