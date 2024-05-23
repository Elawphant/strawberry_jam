
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

    from graph_api.gql.inputs.author_create_input import AuthorCreateInput

    from graph_api.gql.inputs.book_info_create_input import BookInfoCreateInput

    from graph_api.gql.inputs.shelf_create_input import ShelfCreateInput




@strawberry_django.input(Book)
class BookCreateInput:
    id: auto

    add_to_authors_connection: List[Annotated["AuthorCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_create_input"
    )]] = strawberry.field(default_factory=list)
    remove_from_authors_connection: List[Annotated["AuthorCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_create_input"
    )]] = strawberry.field(default_factory=list)

    bookinfo: Annotated["BookInfoCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_info_create_input"
    )]

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    shelf: Annotated["ShelfCreateInput", strawberry.lazy(
        "graph_api.gql.inputs.shelf_create_input"
    )]



