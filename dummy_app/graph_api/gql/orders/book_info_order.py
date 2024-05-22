
    id: auto


    book: Annotated["BookInfo", strawberry.lazy(
        "graph_api.gql.book_info_node"
    )]


    title: auto


    subtitle: auto


    pages: auto


    is_novel: auto


    publication_date: auto

