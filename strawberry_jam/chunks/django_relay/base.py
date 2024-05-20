

todo_comments = """
# TODO: Strawberry-Jam: Remove unused imports
# TODO: Strawberry-Jam: Check the generated schema 
"""

imports = """
import strawberry
import strawberry_django
"""

# model imports must be indented for TYPE_CHECKING, because all models will be imported lazily
model_import = """
    from {model_app_label}.models import {model_name_pascal_case}
"""

# dependency imports must be indented for TYPE_CHECKING, because all dependencies will be imported lazily
api_dependency_import = """
    from {schema_app_label}.{api_folder_name}.{dependency_folder_snake_case}.{dependency_name_snake_case} import {dependency_name_pascal_case}
"""

type_checking = """
if TYPE_CHECKING:
{type_checking_imports}
"""

schema = """
schema = strawberry.Schema(query=Query)
"""

indent = "    "