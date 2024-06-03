
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import List
from library.models import Book



@strawberry_django.input(Book)
class BookCreateInput:

    authors_add: List[strawberry.relay.GlobalID] = strawberry.field(
        default_factory=list,
    )
    authors_remove: List[
        strawberry.relay.GlobalID
    ] = strawberry.field(
        default_factory=list, 
    )
    # alternative implemenattion 
    # authors: strawberry.auto = strawberry_django.field()

    bookinfo: strawberry.auto = strawberry_django.field()

    shelf: strawberry.auto = strawberry_django.field()



