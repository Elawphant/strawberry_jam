
# TODO: Strawberry-Jam: review this file
from django import forms
from strawberry_jam.forms import ModelForm
from library.models import Shelf
from graph_api.gql.nodes.shelf_node import ShelfNode
from graph_api.gql.query_set_managers.shelf_query_set_manager import ShelfQuerySetManager


from graph_api.gql.query_set_managers.book_query_set_manager import BookQuerySetManager


class ShelfCreateForm(ModelForm):

    def __init__(self, info, data, *args, **kwargs) -> None:
        
        self.add_to_books_connection = forms.ModelMultipleChoiceField(queryset=BookQuerySetManager.get_queryset(self.info), required=False)

        self.remove_from_books_connection = forms.ModelMultipleChoiceField(queryset=BookQuerySetManager.get_queryset(self.info), required=False)

        super().__init__(info, data, *args, **kwargs)


    class Meta:
        model = Shelf
        fields = ['number']
        queryset_manager = ShelfQuerySetManager

