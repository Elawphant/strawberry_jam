
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount
from typing import TYPE_CHECKING, Annotated
from library.models import BookInfo
from graph_api.gql.filters.book_info_filter import BookInfoFilter
from graph_api.gql.orders.book_info_order import BookInfoOrder



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(BookInfo, filters=BookInfoFilter, order=BookInfoOrder, fields=["id"])
class BookInfoNode(Node):

    book: Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = strawberry_django.node()


    title: strawberry.auto = strawberry_django.field()


    subtitle: strawberry.auto = strawberry_django.field()


    pages: strawberry.auto = strawberry_django.field()


    is_novel: strawberry.auto = strawberry_django.field()


    publication_date: strawberry.auto = strawberry_django.field()

