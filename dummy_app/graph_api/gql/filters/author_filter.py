

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



if TYPE_CHECKING:
None


@strawberry_django.filter(Author, lookup=True)
class AuthorFilter:



# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.order(Author)
class AuthorOrder:


    id: strawberry.auto


    name: strawberry.auto


    books_connection: List[Annotated["Author", strawberry.lazy(
        "graph_api.gql.author_node"
    )]]

