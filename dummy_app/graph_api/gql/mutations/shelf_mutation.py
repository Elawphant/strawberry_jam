
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry_jam.mutations import create, update
from typing import cast, TYPE_CHECKING, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from graph_api.gql.inputs.shelf_create_input import ShelfCreateInput
from graph_api.gql.inputs.shelf_update_input import ShelfUpdateInput

if TYPE_CHECKING:
    from graph_api.gql.nodes.shelf_node import ShelfNode

@strawberry.type(name="Mutation")
class ShelfMutation:
    create_shelf: Annotated['ShelfNode', strawberry.lazy(
        "graph_api.gql.nodes.shelf_node"
    )] = create(
        ShelfCreateInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]
    )

    update_shelf: Annotated['ShelfNode', strawberry.lazy(
        "graph_api.gql.nodes.shelf_node"
    )] = update(
        ShelfUpdateInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]
    )

    delete_shelf: Annotated['ShelfNode', strawberry.lazy(
        "graph_api.gql.nodes.shelf_node"
    )] = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]

    )

