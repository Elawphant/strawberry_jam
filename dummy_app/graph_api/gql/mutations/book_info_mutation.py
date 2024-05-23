
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import cast

from graph_api.gql.nodes.book_info_node import BookInfoNode
from graph_api.gql.inputs.book_info_create_input import BookInfoCreateInput
from graph_api.gql.inputs.book_info_update_input import BookInfoUpdateInput
from graph_api.gql.forms.book_info_create_form import BookInfoCreateForm
from graph_api.gql.forms.book_info_update_form import BookInfoUpdateForm

@strawberry.type(name="Mutation")
class BookInfoMutation:
    @strawberry_django.mutation(handle_django_errors=True)
    def create_BookInfo(self, data: BookInfoCreateInput):
        form = BookInfoCreateForm(data)
        return cast(BookInfoNode, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_BookInfo(self, data: BookInfoUpdateInput):
        form = BookInfoUpdateForm(data)
        return cast(BookInfoNode, form.save())

    delete_BookInfo: BookInfoNode = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

