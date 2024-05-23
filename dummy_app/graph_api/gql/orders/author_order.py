
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from library.models import Author

@strawberry_django.order(Author)
class AuthorOrder:
    id: auto
    id: auto

    name: auto

    authors_connection: auto

