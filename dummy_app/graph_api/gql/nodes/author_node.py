
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Author
from graph_api.gql.filters.author_filter import AuthorFilter
from graph_api.gql.orders.author_order import AuthorOrder


if TYPE_CHECKING:

    from graph_api.gql.nodes.author_node import AuthorNode




@strawberry_django.type(Author, filters=AuthorFilter, order=AuthorOrder)
class AuthorNode(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    authors_connection: List[Annotated["AuthorNode", strawberry.lazy(
        "graph_api.gql.nodes.author_node"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



