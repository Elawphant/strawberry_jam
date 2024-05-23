
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Book
from graph_api.gql.filters.book_filter import BookFilter
from graph_api.gql.orders.book_order import BookOrder


if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode


    from graph_api.gql.nodes.book_node import BookNode


    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Book, filters=BookFilter, order=BookOrder)
class BookNode(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]


    books_connection: List[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    bookinfo: Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    shelf: Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



