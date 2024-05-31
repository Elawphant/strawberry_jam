
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from strawberry_django.permissions import (
    IsAuthenticated,
)

from library.models import Shelf



@strawberry_django.input(Shelf)
class ShelfUpdateInput:
    id: strawberry.auto

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

    number: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )



