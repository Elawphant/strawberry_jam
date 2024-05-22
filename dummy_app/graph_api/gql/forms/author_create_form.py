

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



from strawberry_jam import ModelForm


from library.models import Author


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = [None]


