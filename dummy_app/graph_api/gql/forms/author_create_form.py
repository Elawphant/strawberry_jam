
# TODO: Strawberry-Jam: review this file
from django import forms
from strawberry_jam.forms import ModelForm
from library.models import Author
from graph_api.gql.nodes.author_node import AuthorNode
from graph_api.gql.query_set_managers.author_query_set_manager import AuthorQuerySetManager


from graph_api.gql.query_set_managers.book_query_set_manager import BookQuerySetManager


class AuthorCreateForm(ModelForm):

    def __init__(self, info, data, *args, **kwargs) -> None:
        
        self.add_to_books_connection = forms.ModelMultipleChoiceField(queryset=BookQuerySetManager.get_queryset(self.info), required=True)

        self.remove_from_books_connection = forms.ModelMultipleChoiceField(queryset=BookQuerySetManager.get_queryset(self.info), required=True)

        super().__init__(info, data, *args, **kwargs)


    class Meta:
        model = Author
        fields = ['name']
        queryset_manager = AuthorQuerySetManager

