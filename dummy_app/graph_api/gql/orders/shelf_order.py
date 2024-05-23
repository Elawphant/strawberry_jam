
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import Shelf


if TYPE_CHECKING:

    from graph_api.gql.orders.book_order import BookOrder



@strawberry_django.order(Shelf)
class ShelfOrder:

    books_connection: List[Annotated["BookOrder", strawberry.lazy(
        "graph_api.gql.orders.book_order"
    )]] | None

    id: auto

    number: auto

