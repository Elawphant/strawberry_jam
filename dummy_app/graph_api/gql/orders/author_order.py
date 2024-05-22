
    id: auto


    name: auto


    books_connection: List[Annotated["Author", strawberry.lazy(
        "graph_api.gql.author_node"
    )]]

