
# TODO: Strawberry-Jam: review this file
from django import forms
from strawberry_jam.forms import ModelForm
from library.models import Book
from graph_api.gql.nodes.book_node import BookNode
from graph_api.gql.query_set_managers.book_query_set_manager import BookQuerySetManager


from graph_api.gql.query_set_managers.author_query_set_manager import AuthorQuerySetManager

from graph_api.gql.query_set_managers.book_info_query_set_manager import BookInfoQuerySetManager

from graph_api.gql.query_set_managers.shelf_query_set_manager import ShelfQuerySetManager


class BookCreateForm(ModelForm):

    def __init__(self, info, data, *args, **kwargs) -> None:
        
        self.add_to_authors_connection = forms.ModelMultipleChoiceField(queryset=AuthorQuerySetManager.get_queryset(self.info), required=False)

        self.remove_from_authors_connection = forms.ModelMultipleChoiceField(queryset=AuthorQuerySetManager.get_queryset(self.info), required=False)

        self.bookinfo = forms.ModelChoiceField(queryset=BookInfoQuerySetManager.get_queryset(self.info))

        self.shelf = forms.ModelChoiceField(queryset=ShelfQuerySetManager.get_queryset(self.info))

        super().__init__(info, data, *args, **kwargs)


    class Meta:
        model = Book
        fields = []
        queryset_manager = BookQuerySetManager

