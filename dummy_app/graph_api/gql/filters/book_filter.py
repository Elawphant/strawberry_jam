
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import Book


if TYPE_CHECKING:

    from graph_api.gql.filters.author_filter import AuthorFilter

    from graph_api.gql.filters.book_info_filter import BookInfoFilter

    from graph_api.gql.filters.shelf_filter import ShelfFilter



@strawberry_django.filter(Book, lookups=True)
class BookFilter:

    authors_connection: List[Annotated["AuthorFilter", strawberry.lazy(
        "graph_api.gql.filters.author_filter"
    )]] | None

    bookinfo: List[Annotated["BookInfoFilter", strawberry.lazy(
        "graph_api.gql.filters.book_info_filter"
    )]] | None

    id: auto

    shelf: List[Annotated["ShelfFilter", strawberry.lazy(
        "graph_api.gql.filters.shelf_filter"
    )]] | None

