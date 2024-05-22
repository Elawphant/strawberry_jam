
from graph_api.None.forms.book_update_form import BookUpdateForm


@strawberry.type(name="Mutation")
class BookMutation:

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = BookCreateForm(data)
        return cast(BookNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = BookUpdateForm(data)
        return cast(BookNode, form.save())

    delete_None: BookNode = strawberry_django.mutations.None(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )


