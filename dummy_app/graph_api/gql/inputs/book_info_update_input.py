

# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 


import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated



@strawberry_django.input(BookInfo)
class BookInfoUpdateInputPartial(strawberry_django.NodeInput):


    id: auto


    book: Annotated["BookInfo", strawberry.lazy(
        "graph_api.gql.book_info_node"
    )]


    title: auto


    subtitle: auto


    pages: auto


    is_novel: auto


    publication_date: auto

