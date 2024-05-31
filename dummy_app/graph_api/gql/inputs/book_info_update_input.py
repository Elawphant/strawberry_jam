
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import BookInfo



@strawberry_django.input(BookInfo)
class BookInfoUpdateInput:
    id: strawberry.auto

    book: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    title: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    subtitle: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    pages: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    is_novel: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    publication_date: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



