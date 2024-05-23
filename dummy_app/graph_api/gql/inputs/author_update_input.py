
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Author

if TYPE_CHECKING:

    from graph_api.gql.inputs.author_update_input import AuthorUpdateInput




@strawberry_django.input(Author)
class AuthorUpdateInput:
    id: auto

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    add_to_authors_connection: List[Annotated["AuthorUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_update_input"
    )]] = strawberry.field(default_factory=list)
    remove_from_authors_connection: List[Annotated["AuthorUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.author_update_input"
    )]] = strawberry.field(default_factory=list)



