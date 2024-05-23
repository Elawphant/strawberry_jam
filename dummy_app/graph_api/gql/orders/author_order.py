
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import Author


if TYPE_CHECKING:

    from graph_api.gql.orders.book_order import BookOrder



@strawberry_django.order(Author)
class AuthorOrder:

    id: auto

    name: auto

    books_connection: List[Annotated["BookOrder", strawberry.lazy(
        "graph_api.gql.orders.book_order"
    )]] | None

