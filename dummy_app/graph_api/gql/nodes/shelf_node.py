
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)
from strawberry_jam.node import Node
from library.models import Shelf
from graph_api.gql.filters.shelf_filter import ShelfFilter
from graph_api.gql.orders.shelf_order import ShelfOrder
from graph_api.gql.query_set_managers.shelf_query_set_manager import ShelfQuerySetManager



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Shelf, filters=ShelfFilter, order=ShelfOrder)
class ShelfNode(Node):

    books_connection: List[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.connection(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    class Meta:
        queryset_manager = ShelfQuerySetManager

