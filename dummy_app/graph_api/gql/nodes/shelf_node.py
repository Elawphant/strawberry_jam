
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Shelf
from graph_api.gql.filters.shelf_filter import ShelfFilter
from graph_api.gql.orders.shelf_order import ShelfOrder


if TYPE_CHECKING:

    from graph_api.gql.nodes.shelf_node import ShelfNode




@strawberry_django.type(Shelf, filters=ShelfFilter, order=ShelfOrder)
class ShelfNode(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]


    shelfs_connection: List[Annotated["ShelfNode", strawberry.lazy(
        "graph_api.gql.nodes.shelf_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



