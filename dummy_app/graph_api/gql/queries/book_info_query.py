
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from graph_api.gql.nodes.book_info_node import BookInfoNode

@strawberry.type(name="Query")
class BookInfoQuery:
    book_infos_connection: strawberry_django.relay.ListConnectionWithTotalCount[BookInfoNode] = strawberry_django.connection()
