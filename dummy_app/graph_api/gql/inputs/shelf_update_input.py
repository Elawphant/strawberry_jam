
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from library.models import Shelf



@strawberry_django.input(Shelf, partial=True)
class ShelfUpdateInput:
    id: strawberry.auto

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

    number: strawberry.auto = strawberry_django.field()



