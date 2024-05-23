
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from library.models import Author


class ('AuthorUpdateForm',)(ModelForm):
    class Meta:
        model = Author
        fields = [id, name, books]

