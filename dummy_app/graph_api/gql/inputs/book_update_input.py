

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(Book)
class BookUpdateInputPartial(strawberry_django.NodeInput):


    add_to_authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]]
    remove_from_authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]]
    


    bookinfo: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]


    id: auto


    shelf: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]

