
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount
from typing import TYPE_CHECKING, Annotated
from library.models import Author
from graph_api.gql.filters.author_filter import AuthorFilter
from graph_api.gql.orders.author_order import AuthorOrder



if TYPE_CHECKING:

    from graph_api.gql.nodes.book_node import BookNode




@strawberry_django.type(Author, filters=AuthorFilter, order=AuthorOrder, fields=["id"])
class AuthorNode(Node):

    name: strawberry.auto = strawberry_django.field()


    books_connection: ListConnectionWithTotalCount[Annotated["BookNode", strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )]] = strawberry_django.connection(
        field_name="books",
    )

