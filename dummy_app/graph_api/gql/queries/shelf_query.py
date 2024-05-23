
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from graph_api.gql.nodes.shelf_node import ShelfNode

@strawberry.type(name="Query")
class ShelfQuery:
    shelfs_connection: strawberry_django.relay.ListConnectionWithTotalCount[ShelfNode] = strawberry_django.connection()
