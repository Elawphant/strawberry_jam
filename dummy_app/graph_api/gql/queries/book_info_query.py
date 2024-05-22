

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry.type(name="Query")
class BookInfoQuery:


    None: strawberry_django.relay.ListConnectionWithTotalCount[BookInfoNode] = strawberry_django.connection()

