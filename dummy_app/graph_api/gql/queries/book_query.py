
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from graph_api.gql.nodes.book_node import BookNode

@strawberry.type(name="Query")
class BookQuery:
    books_connection: strawberry_django.relay.ListConnectionWithTotalCount[BookNode] = strawberry_django.connection()
