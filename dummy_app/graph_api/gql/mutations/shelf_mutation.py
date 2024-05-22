
from graph_api.None.forms.shelf_update_form import ShelfUpdateForm


@strawberry.type(name="Mutation")
class ShelfMutation:

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = ShelfCreateForm(data)
        return cast(ShelfNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = ShelfUpdateForm(data)
        return cast(ShelfNode, form.save())

    delete_None: ShelfNode = strawberry_django.mutations.None(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )


