# TODO


imports = """
import strawberry_django
"""

type_class = """
@strawberry_django.order({model_name_pascal_case})
class {model_name_pascal_case}Order:
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
    {field_name_snake_case}: List[Annotated["{model_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]]
"""