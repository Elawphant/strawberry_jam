
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)
from strawberry_jam.node import Node
from library.models import Author
from graph_api.gql.filters.author_filter import AuthorFilter
from graph_api.gql.orders.author_order import AuthorOrder
from graph_api.gql.query_set_managers.author_query_set_manager import AuthorQuerySetManager



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Author, filters=AuthorFilter, order=AuthorOrder)
class AuthorNode(Node):

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    books_connection: List[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.connection(
        extensions=[IsAuthenticated()],
    )


    class Meta:
        queryset_manager = AuthorQuerySetManager

