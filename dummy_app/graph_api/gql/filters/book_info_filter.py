

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


@strawberry_django.filter(BookInfo, lookup=True)
class BookInfoFilter:



# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.order(BookInfo)
class BookInfoOrder:


    id: strawberry.auto


    book: Annotated["BookInfo", strawberry.lazy(
        "graph_api.gql.book_info_node"
    )]


    title: strawberry.auto


    subtitle: strawberry.auto


    pages: strawberry.auto


    is_novel: strawberry.auto


    publication_date: strawberry.auto

