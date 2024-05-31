
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Book



@strawberry_django.input(Book)
class BookUpdateInput:
    id: strawberry.auto

    authors_add: List[strawberry.relay.GlobalID] = strawberry.field(
        default_factory=list,
        extensions=[IsAuthenticated()]
    )
    authors_remove: List[
        strawberry.relay.GlobalID
    ] = strawberry.field(
        default_factory=list, 
        extensions=[IsAuthenticated()]
    )
    # alternative implemenattion 
    # authors: strawberry.auto = strawberry_django.field(
    #     extensions=[IsAuthenticated()],
    # )

    bookinfo: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )

    shelf: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



