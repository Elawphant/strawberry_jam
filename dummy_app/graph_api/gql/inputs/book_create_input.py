

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(Book)
class BookCreateInput:


    add_to_authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]] = strawberry.field(default_factory=list)
    remove_from_authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]] = strawberry.field(default_factory=list)
    


    bookinfo: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]


    id: auto


    shelf: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]

