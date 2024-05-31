
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry_jam.mutations import create, update
from typing import cast, TYPE_CHECKING, Annotated

from graph_api.gql.inputs.author_create_input import AuthorCreateInput
from graph_api.gql.inputs.author_update_input import AuthorUpdateInput

if TYPE_CHECKING:
    from graph_api.gql.nodes.author_node import AuthorNode

@strawberry.type(name="Mutation")
class AuthorMutation:
    create_author: Annotated['AuthorNode', strawberry.lazy(
        "graph_api.gql.nodes.author_node"
    )] = create(
        AuthorCreateInput,
        handle_django_errors=True
    )

    update_author: Annotated['AuthorNode', strawberry.lazy(
        "graph_api.gql.nodes.author_node"
    )] = update(
        AuthorUpdateInput,
        handle_django_errors=True
    )

    delete_author: Annotated['AuthorNode', strawberry.lazy(
        "graph_api.gql.nodes.author_node"
    )] = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

