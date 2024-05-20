


type_class = """
@strawberry_django.input({model_name_pascal_case})
class {update_input_name_pascal_case}Partial(strawberry_django.NodeInput):
"""

field = """
    {field_name_snake_case}: auto
"""

relation_to_one = """
    {field_name_snake_case}: Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]
"""

relation_to_many = """
    add_to_{field_name_snake_case}: List[Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]]
    remove_from_{field_name_snake_case}: List[Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]]
    
"""