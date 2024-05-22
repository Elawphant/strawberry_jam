

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(Shelf)
class ShelfCreateInput:


    add_to_books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]] = strawberry.field(default_factory=list)
    remove_from_books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]] = strawberry.field(default_factory=list)
    


    id: auto


    number: auto
