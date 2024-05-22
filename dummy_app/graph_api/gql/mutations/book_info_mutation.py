
from graph_api.None.forms.book_info_update_form import BookInfoUpdateForm


@strawberry.type(name="Mutation")
class BookInfoMutation:

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = BookInfoCreateForm(data)
        return cast(BookInfoNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = BookInfoUpdateForm(data)
        return cast(BookInfoNode, form.save())

    delete_None: BookInfoNode = strawberry_django.mutations.None(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )


