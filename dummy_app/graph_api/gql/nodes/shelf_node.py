
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount
from typing import TYPE_CHECKING, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)
from library.models import Shelf
from graph_api.gql.filters.shelf_filter import ShelfFilter
from graph_api.gql.orders.shelf_order import ShelfOrder



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Shelf, filters=ShelfFilter, order=ShelfOrder)
class ShelfNode(Node):

    books_connection: ListConnectionWithTotalCount[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.connection(
        field_name="books",
        extensions=[IsAuthenticated()],
    )


    id: strawberry.relay.GlobalID = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


