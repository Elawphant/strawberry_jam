
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

    from graph_api.gql.inputs.author_update_input import AuthorUpdateInput

    from graph_api.gql.inputs.book_info_update_input import BookInfoUpdateInput

    from graph_api.gql.inputs.shelf_update_input import ShelfUpdateInput




@strawberry_django.input(Book)
class BookUpdateInput:
    id: auto

    add_to_authors_connection: List[Annotated["AuthorUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_update_input"
    )]] = strawberry.field(default_factory=list)
    remove_from_authors_connection: List[Annotated["AuthorUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_update_input"
    )]] = strawberry.field(default_factory=list)

    bookinfo: Annotated["BookInfoUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.book_info_update_input"
    )]

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    shelf: Annotated["ShelfUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.shelf_update_input"
    )]



