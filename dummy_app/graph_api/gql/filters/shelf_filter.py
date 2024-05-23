
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import Shelf


if TYPE_CHECKING:

    from graph_api.gql.filters.book_filter import BookFilter



@strawberry_django.filter(Shelf, lookups=True)
class ShelfFilter:

    books_connection: List[Annotated["BookFilter", strawberry.lazy(
        "graph_api.gql.filters.book_filter"
    )]] | None

    id: auto

    number: auto

