
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import cast

from graph_api.gql.nodes.book_node import BookNode
from graph_api.gql.inputs.book_create_input import BookCreateInput
from graph_api.gql.inputs.book_update_input import BookUpdateInput
from graph_api.gql.forms.book_create_form import BookCreateForm
from graph_api.gql.forms.book_update_form import BookUpdateForm

@strawberry.type(name="Mutation")
class BookMutation:
    @strawberry_django.mutation(handle_django_errors=True)
    def create_book(self, data: BookCreateInput) -> BookNode:
        form = BookCreateForm(data)
        return cast(BookNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_book(self, data: BookUpdateInput) -> BookNode:
        form = BookUpdateForm(data)
        return cast(BookNode, form.save())

    delete_book: BookNode = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

