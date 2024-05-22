

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(Shelf)
class ShelfUpdateInputPartial(strawberry_django.NodeInput):


    add_to_books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]]
    remove_from_books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]]
    


    id: auto


    number: auto

