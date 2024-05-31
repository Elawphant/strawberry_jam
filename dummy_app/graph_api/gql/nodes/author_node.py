
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount
from typing import TYPE_CHECKING, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)
from library.models import Author
from graph_api.gql.filters.author_filter import AuthorFilter
from graph_api.gql.orders.author_order import AuthorOrder



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Author, filters=AuthorFilter, order=AuthorOrder)
class AuthorNode(strawberry.relay.Node):

    id: strawberry.relay.GlobalID = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    books_connection: ListConnectionWithTotalCount[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.connection(
        field_name="books",
        extensions=[IsAuthenticated()],
    )


