

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(Author)
class AuthorCreateInput:


    id: auto


    name: auto


    add_to_books_connection: List[Annotated["Author", strawberry.lazy(
        "graph_api.gql.author_node"
    )]] = strawberry.field(default_factory=list)
    remove_from_books_connection: List[Annotated["Author", strawberry.lazy(
        "graph_api.gql.author_node"
    )]] = strawberry.field(default_factory=list)
    

