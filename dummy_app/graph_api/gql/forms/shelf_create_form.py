
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from library.models import Shelf


class ShelfCreateForm(ModelForm):
    class Meta:
        model = Shelf
        fields = ['books', 'number']

