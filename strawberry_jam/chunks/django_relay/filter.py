
type_class = """
@strawberry_django.filter({model_name_pascal_case}, lookup=True)
class {filter_name_pascal_case}:
"""

field = """
    {field_name_snake_case}: strawberry.auto
"""

relation_to_one = """
    {field_name_snake_case}: Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]
"""

relation_to_many = """
    {field_name_snake_case}: List[Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]]
"""