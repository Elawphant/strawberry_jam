
# TODO: Strawberry-Jam: review this file
import strawberry_django
import strawberry
from strawberry import auto, relay
from typing import TYPE_CHECKING, List, Annotated

from library.models import BookInfo


if TYPE_CHECKING:

    from graph_api.gql.filters.book_filter import BookFilter



@strawberry_django.filter(BookInfo, lookups=True)
class BookInfoFilter:

    id: auto

    book: List[Annotated["BookFilter", strawberry.lazy(
        "graph_api.gql.filters.book_filter"
    )]] | None

    title: auto

    subtitle: auto

    pages: auto

    is_novel: auto

    publication_date: auto

