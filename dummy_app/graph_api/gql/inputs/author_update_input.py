
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from library.models import Author



@strawberry_django.input(Author, partial=True)
class AuthorUpdateInput:
    id: strawberry.auto

    name: strawberry.auto = strawberry_django.field()

    books_add: List[strawberry.relay.GlobalID] = strawberry.field(
        default_factory=list,
    )
    books_remove: List[
        strawberry.relay.GlobalID
    ] = strawberry.field(
        default_factory=list, 
    )
    # alternative implemenattion 
    # books: strawberry.auto = strawberry_django.field()



