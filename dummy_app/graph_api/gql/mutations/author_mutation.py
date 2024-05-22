
from graph_api.None.forms.author_update_form import AuthorUpdateForm


@strawberry.type(name="Mutation")
class AuthorMutation:

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = AuthorCreateForm(data)
        return cast(AuthorNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_None(self, data: dict):
        form = AuthorUpdateForm(data)
        return cast(AuthorNode, form.save())

    delete_None: AuthorNode = strawberry_django.mutations.None(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )


