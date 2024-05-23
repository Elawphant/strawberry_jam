
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Shelf

if TYPE_CHECKING:

    from graph_api.gql.inputs.shelf_update_input import ShelfUpdateInput




@strawberry_django.input(Shelf)
class ShelfUpdateInput:
    id: auto

    add_to_shelfs_connection: List[Annotated["ShelfUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.shelf_update_input"
    )]] = strawberry.field(default_factory=list)
    remove_from_shelfs_connection: List[Annotated["ShelfUpdateInput", strawberry.lazy(
        "graph_api.gql.inputs.shelf_update_input"
    )]] = strawberry.field(default_factory=list)

    id: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



