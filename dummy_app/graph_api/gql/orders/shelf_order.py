
    books_connection: List[Annotated["Shelf", strawberry.lazy(
        "graph_api.gql.shelf_node"
    )]]


    id: auto


    number: auto

