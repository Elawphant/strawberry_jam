
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import Book


if TYPE_CHECKING:

    from graph_api.gql.orders.author_order import AuthorOrder

    from graph_api.gql.orders.book_info_order import BookInfoOrder

    from graph_api.gql.orders.shelf_order import ShelfOrder



@strawberry_django.order(Book)
class BookOrder:

    authors_connection: List[Annotated["AuthorOrder", strawberry.lazy(
        "graph_api.gql.orders.author_order"
    )]] | None

    bookinfo: List[Annotated["BookInfoOrder", strawberry.lazy(
        "graph_api.gql.orders.book_info_order"
    )]] | None

    id: auto

    shelf: List[Annotated["ShelfOrder", strawberry.lazy(
        "graph_api.gql.orders.shelf_order"
    )]] | None

