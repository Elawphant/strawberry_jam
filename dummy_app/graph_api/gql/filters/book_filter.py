

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


@strawberry_django.filter(Book, lookup=True)
class BookFilter:



# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.order(Book)
class BookOrder:


    authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]]


    bookinfo: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]


    id: strawberry.auto


    shelf: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]

