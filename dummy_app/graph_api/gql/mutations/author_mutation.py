
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django

from graph_api.gql.mutations.nodes.author_node import ('Author',)('Node',)
from graph_api.gql.mutations.inputs.author_create_input import ('Author',)('CreateInput',)
from graph_api.gql.mutations.inputs.author_update_input import ('Author',)('UpdateInput',)
from graph_api.gql.mutations.forms.author_update_form import ('Author',)('CreateForm',)
from graph_api.gql.mutations.forms.author_update_form import ('Author',)('UpdateForm',)

@strawberry.type(name="Mutation")
class ('AuthorMutation',):
    @strawberry_django.mutation(handle_django_errors=True)
    def create_Author(self, data: ('Author',)('CreateInput',)):
        form = ('Author',)('CreateForm',)(data)
        return cast(('Author',)('Node',), form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_Author(self, data: ('Author',)('UpdateInput',)):
        form = ('Author',)('UpdateForm',)(data)
        return cast(('Author',)('Node',), form.save())

    delete_Author: ('Author',)('Node',) = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

