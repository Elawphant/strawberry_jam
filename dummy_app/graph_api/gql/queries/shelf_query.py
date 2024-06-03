
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry_django.permissions import (
    IsAuthenticated,
)
from graph_api.gql.nodes.shelf_node import ShelfNode

@strawberry.type(name="Query")
class ShelfQuery:
    shelfs_connection: strawberry_django.relay.ListConnectionWithTotalCount[ShelfNode] = strawberry_django.connection(
        extensions=[
            IsAuthenticated(),
        ]
    )
