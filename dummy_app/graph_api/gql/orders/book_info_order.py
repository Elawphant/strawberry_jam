
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import BookInfo


if TYPE_CHECKING:

    from graph_api.gql.orders.book_order import BookOrder



@strawberry_django.order(BookInfo)
class BookInfoOrder:

    id: auto

    book: List[Annotated["BookOrder", strawberry.lazy(
        "graph_api.gql.orders.book_order"
    )]] | None

    title: auto

    subtitle: auto

    pages: auto

    is_novel: auto

    publication_date: auto

