
import strawberry

from graph_api.gql.queries.book_query import BookQuery

from graph_api.gql.queries.shelf_query import ShelfQuery

from graph_api.gql.queries.book_info_query import BookInfoQuery

from graph_api.gql.queries.author_query import AuthorQuery


@strawberry.type
class Query(
    BookQuery,
    ShelfQuery,
    BookInfoQuery,
    AuthorQuery
    ): 
    node: strawberry.relay.Node = strawberry.relay.node()
    
@strawberry.type
class Mutation(

): pass
    
schema = strawberry.Schema(query=Query, )

