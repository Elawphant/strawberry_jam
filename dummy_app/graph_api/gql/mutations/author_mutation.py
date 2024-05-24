
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import cast

from graph_api.gql.nodes.author_node import AuthorNode
from graph_api.gql.inputs.author_create_input import AuthorCreateInput
from graph_api.gql.inputs.author_update_input import AuthorUpdateInput
from graph_api.gql.forms.author_create_form import AuthorCreateForm
from graph_api.gql.forms.author_update_form import AuthorUpdateForm

@strawberry.type(name="Mutation")
class AuthorMutation:
    @strawberry_django.mutation(handle_django_errors=True)
    def create_author(self, info, data: AuthorCreateInput) -> AuthorNode:
        form = AuthorCreateForm(data, info)
        return cast(AuthorNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_author(self, info, data: AuthorUpdateInput) -> AuthorNode:
        form = AuthorUpdateForm(data)
        return cast(AuthorNode, form.save())

    delete_author: AuthorNode = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

