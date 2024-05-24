
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import cast

from graph_api.gql.nodes.shelf_node import ShelfNode
from graph_api.gql.inputs.shelf_create_input import ShelfCreateInput
from graph_api.gql.inputs.shelf_update_input import ShelfUpdateInput
from graph_api.gql.forms.shelf_create_form import ShelfCreateForm
from graph_api.gql.forms.shelf_update_form import ShelfUpdateForm

@strawberry.type(name="Mutation")
class ShelfMutation:
    @strawberry_django.mutation(handle_django_errors=True)
    def create_shelf(self, info, data: ShelfCreateInput) -> ShelfNode:
        form = ShelfCreateForm(data, info)
        return cast(ShelfNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_shelf(self, info, data: ShelfUpdateInput) -> ShelfNode:
        form = ShelfUpdateForm(data)
        return cast(ShelfNode, form.save())

    delete_shelf: ShelfNode = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

