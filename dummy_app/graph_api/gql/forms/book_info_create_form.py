
# TODO: Strawberry-Jam: review this file
from django import forms
from strawberry_jam.forms import ModelForm
from library.models import BookInfo
from graph_api.gql.nodes.book_info_node import BookInfoNode
from graph_api.gql.query_set_managers.book_info_query_set_manager import BookInfoQuerySetManager


from graph_api.gql.query_set_managers.book_query_set_manager import BookQuerySetManager


class BookInfoCreateForm(ModelForm):

    def __init__(self, info, data, *args, **kwargs) -> None:
        
        self.book = forms.ModelChoiceField(queryset=BookQuerySetManager.get_queryset(self.info))

        super().__init__(info, data, *args, **kwargs)


    class Meta:
        model = BookInfo
        fields = ['title', 'subtitle', 'pages', 'is_novel', 'publication_date']
        queryset_manager = BookInfoQuerySetManager

