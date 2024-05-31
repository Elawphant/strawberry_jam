
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Author



@strawberry_django.input(Author)
class AuthorUpdateInput:
    id: strawberry.auto

    name: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    books_add: List[strawberry.relay.GlobalID] = strawberry.field(
        default_factory=list,
        extensions=[IsAuthenticated()]
    )
    books_remove: List[
        strawberry.relay.GlobalID
    ] = strawberry.field(
        default_factory=list, 
        extensions=[IsAuthenticated()]
    )
    # alternative implemenattion 
    # books: strawberry.auto = strawberry_django.field(
    #     extensions=[IsAuthenticated()],
    # )



