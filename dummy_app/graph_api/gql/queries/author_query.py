
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from graph_api.gql.nodes.author_node import AuthorNode

@strawberry.type(name="Query")
class AuthorQuery:
    authors_connection: strawberry_django.relay.ListConnectionWithTotalCount[AuthorNode] = strawberry_django.connection()
