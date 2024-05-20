imports = """
from strawberry_django.permissions import (
    IsAuthenticated,
)
"""


type_class = """
@strawberry_django.type({model_name_pascal_case}, filters={filter_name_pascal_case})
class {node_name_pascal_case}(strawberry.relay.Node):
    code: relay.NodeID[int]
"""

field = """
    {field_name_snake_case}: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )
"""

relation_to_one = """
    {field_name_snake_case}: Annotated["{field_node_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{field_node_name_snake_case}"
    )] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )
"""

relation_to_many = """
    {field_name_snake_case}: List[Annotated["{field_node_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{node_name_snake_case}"
    )]] = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )
"""