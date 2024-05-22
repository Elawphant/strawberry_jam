

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


from strawberry_django.permissions import (
    IsAuthenticated,
)


@strawberry_django.type(BookInfo, filters=BookInfoFilter)
class BookInfoNode(strawberry.relay.Node):
    code: relay.NodeID[int]


    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )


    book: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book"
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

