
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Book


if TYPE_CHECKING:

    from graph_api.gql.inputs.book_create_input import BookCreateInput

    from graph_api.gql.inputs.book_create_input import BookCreateInput

    from graph_api.gql.inputs.book_create_input import BookCreateInput




@strawberry_django.input(Book)
class BookCreateInput:
    id: auto

    add_to_books_connection: List[Annotated["BookCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_create_input"
    )]] = strawberry.field(default_factory=list)
    remove_from_books_connection: List[Annotated["BookCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_create_input"
    )]] = strawberry.field(default_factory=list)

    bookinfo: Annotated["BookCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_create_input"
    )]

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    shelf: Annotated["BookCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_create_input"
    )]



