

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


@strawberry_django.type(Book, filters=BookFilter)
class BookNode(strawberry.relay.Node):
    code: relay.NodeID[int]


    authors_connection: List[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.book_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    bookinfo: Annotated["Bookinfo", strawberry.lazy(
        "graph_api.gql.bookinfo"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    shelf: Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

