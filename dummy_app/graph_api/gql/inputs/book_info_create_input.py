
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from library.models import BookInfo



@strawberry_django.input(BookInfo)
class BookInfoCreateInput:

    book: strawberry.auto = strawberry_django.field()

    title: strawberry.auto = strawberry_django.field()

    subtitle: strawberry.auto = strawberry_django.field()

    pages: strawberry.auto = strawberry_django.field()

    is_novel: strawberry.auto = strawberry_django.field()

    publication_date: strawberry.auto = strawberry_django.field()



