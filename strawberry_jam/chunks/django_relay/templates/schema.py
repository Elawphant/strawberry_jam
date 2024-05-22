
output = """
import strawberry
{dependency_imports}

@strawberry.type
class Query({comma_separated_list_of_pascal_case_query_names}):
    pass
    
@strawberry.type
class Mutation({comma_separated_list_of_pascal_case_mutation_names}):
    pass
    
schema = strawberry.Schema(query=Query, mutation=Mutation)

"""