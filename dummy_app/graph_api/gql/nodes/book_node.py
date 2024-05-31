
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount
from typing import TYPE_CHECKING, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)
from library.models import Book
from graph_api.gql.filters.book_filter import BookFilter
from graph_api.gql.orders.book_order import BookOrder



if TYPE_CHECKING:

    from graph_api.gql.nodes.author_node import AuthorNode


    from graph_api.gql.nodes.book_info_node import BookInfoNode


    from graph_api.gql.nodes.shelf_node import ShelfNode




@strawberry_django.type(Book, filters=BookFilter, order=BookOrder)
class BookNode(Node):

    authors_connection: ListConnectionWithTotalCount[Annotated["AuthorNode", strawberry.lazy(
        "graph_api.gql.nodes.author_node"
    )]] = strawberry_django.connection(
        field_name="authors",
        extensions=[IsAuthenticated()],
    )


    bookinfo: Annotated["BookInfoNode", strawberry.lazy(
        "graph_api.gql.nodes.book_info_node"
    )] = strawberry_django.node(
        extensions=[IsAuthenticated()],
    )


    id: strawberry.relay.GlobalID = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    shelf: Annotated["ShelfNode", strawberry.lazy(
        "graph_api.gql.nodes.shelf_node"
    )] = strawberry_django.node(
        extensions=[IsAuthenticated()],
    )


