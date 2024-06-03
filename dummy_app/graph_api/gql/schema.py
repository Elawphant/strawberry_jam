
import strawberry

from graph_api.gql.queries.book_query import BookQuery

from graph_api.gql.queries.shelf_query import ShelfQuery

from graph_api.gql.queries.book_info_query import BookInfoQuery

from graph_api.gql.queries.author_query import AuthorQuery

from graph_api.gql.mutations.author_mutation import AuthorMutation

from graph_api.gql.mutations.book_mutation import BookMutation

from graph_api.gql.mutations.shelf_mutation import ShelfMutation

from graph_api.gql.mutations.book_info_mutation import BookInfoMutation


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
    AuthorMutation,
    BookMutation,
    ShelfMutation,
    BookInfoMutation
): pass
    
schema = strawberry.Schema(query=Query, mutation=Mutation)

