

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


@strawberry_django.type(Author, filters=AuthorFilter)
class AuthorNode(strawberry.relay.Node):
    code: relay.NodeID[int]


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    books_connection: List[Annotated["AuthorNode", strawberry.lazy(
        "graph_api.gql.author_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

