
import strawberry


@strawberry.type
class Query(

    ):
    pass
    
@strawberry.type
class Mutation(

    ):
    pass
    
schema = strawberry.Schema(query=Query, mutation=Mutation)

