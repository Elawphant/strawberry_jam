

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


@strawberry_django.filter(Shelf, lookup=True)
class ShelfFilter:



# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.order(Shelf)
class ShelfOrder:


    books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]]


    id: strawberry.auto


    number: strawberry.auto

