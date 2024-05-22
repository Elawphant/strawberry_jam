
    authors_connection: List[Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]]


    bookinfo: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]


    id: auto


    shelf: Annotated["Book", strawberry.lazy(
        "graph_api.gql.book_node"
    )]

