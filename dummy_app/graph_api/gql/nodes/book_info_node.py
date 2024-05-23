
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import BookInfo
from graph_api.gql.filters.book_info_filter import BookInfoFilter
from graph_api.gql.orders.book_info_order import BookInfoOrder


if TYPE_CHECKING:

    from graph_api.gql.nodes.bookinfo_node import BookinfoNode




@strawberry_django.type(BookInfo, filters=BookInfoFilter, order=BookInfoOrder)
class BookInfoNode(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    book: Annotated["BookinfoNode", strawberry.lazy(
        "graph_api.gql.nodes.bookinfo_node"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    title: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    subtitle: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    pages: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    is_novel: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    publication_date: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



