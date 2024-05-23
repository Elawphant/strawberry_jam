
# TODO: Strawberry-Jam: review this file
import strawberry

from graph_api.gql.queries.nodes.author_node import ('Author',)('Node',)

@strawberry.type(name="Query")
class ('AuthorQuery',):
    authors_connection: strawberry_django.relay.ListConnectionWithTotalCount[('Author',)('Node',)] = strawberry_django.connection()
