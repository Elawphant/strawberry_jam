
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import BookInfo


if TYPE_CHECKING:

    from graph_api.gql.inputs.book_create_input import BookCreateInput




@strawberry_django.input(BookInfo)
class BookInfoCreateInput:
    id: auto

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    book: Annotated["BookCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_create_input"
    )]

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



