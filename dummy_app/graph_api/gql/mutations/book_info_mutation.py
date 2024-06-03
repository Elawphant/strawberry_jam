
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry_jam.mutations import create, update
from typing import cast, TYPE_CHECKING, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from graph_api.gql.inputs.book_info_create_input import BookInfoCreateInput
from graph_api.gql.inputs.book_info_update_input import BookInfoUpdateInput

if TYPE_CHECKING:
    from graph_api.gql.nodes.book_info_node import BookInfoNode

@strawberry.type(name="Mutation")
class BookInfoMutation:
    create_book_info: Annotated['BookInfoNode', strawberry.lazy(
        "graph_api.gql.nodes.book_info_node"
    )] = create(
        BookInfoCreateInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]
    )

    update_book_info: Annotated['BookInfoNode', strawberry.lazy(
        "graph_api.gql.nodes.book_info_node"
    )] = update(
        BookInfoUpdateInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]
    )

    delete_book_info: Annotated['BookInfoNode', strawberry.lazy(
        "graph_api.gql.nodes.book_info_node"
    )] = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True,
        extensions=[
            IsAuthenticated(),
        ]

    )

