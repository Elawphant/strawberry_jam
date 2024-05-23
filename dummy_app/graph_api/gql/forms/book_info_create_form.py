
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from library.models import BookInfo


class BookInfoCreateForm(ModelForm):
    class Meta:
        model = BookInfo
        fields = ['book', 'title', 'subtitle', 'pages', 'is_novel', 'publication_date']

