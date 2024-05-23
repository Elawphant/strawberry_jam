
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from library.models import Book


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'bookinfo', 'shelf']

