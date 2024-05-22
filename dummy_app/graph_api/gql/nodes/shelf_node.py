

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


from strawberry_django.permissions import (
    IsAuthenticated,
)


@strawberry_django.type(Shelf, filters=ShelfFilter)
class ShelfNode(strawberry.relay.Node):
    code: relay.NodeID[int]


    books_connection: List[Annotated["ShelfNode", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

