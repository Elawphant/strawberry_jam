
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from strawberry_jam.mutations import create, update
from typing import cast, TYPE_CHECKING, Annotated

from graph_api.gql.inputs.book_create_input import BookCreateInput
from graph_api.gql.inputs.book_update_input import BookUpdateInput

if TYPE_CHECKING:
    from graph_api.gql.nodes.book_node import BookNode

@strawberry.type(name="Mutation")
class BookMutation:
    create_book: Annotated['BookNode', strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = create(
        BookCreateInput,
        handle_django_errors=True
    )

    update_book: Annotated['BookNode', strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = update(
        BookUpdateInput,
        handle_django_errors=True
    )

    delete_book: Annotated['BookNode', strawberry.lazy(
        "graph_api.gql.nodes.book_node"
    )] = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

