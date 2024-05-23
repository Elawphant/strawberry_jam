
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from library.models import Book


class BookUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'bookinfo', 'id', 'shelf']

