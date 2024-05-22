from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.codegen.utils import pascal_case, snake_case
from django.db.models import Field, OneToOneField, ManyToManyField, ForeignKey

TYPE_CHECKING_IMPORTS = """
if TYPE_CHECKING:
{type_checking_imports}
"""

API_DEPENDANCY_IMPORT = """
    from {schema_app_label}.{api_folder_name}.{module_dir_name}.{field_input_module_name} import {field_input_name}
"""


FIELD = """
    {field_name}: strawberry.auto = strawberry_django.field(
        extensions=[IsAuthenticated()],
    )
"""

REL_TO_ONE = """
    {field_name}: Annotated["{field_input_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{module_dir_name}.{field_input_module_dir_name}"
    )]
"""

REL_TO_MANY = """
    add_to_{field_name}: List[Annotated["{field_input_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{module_dir_name}.{field_input_module_dir_name}"
    )]] = strawberry.field(default_factory=list)
    remove_from_{field_name}: List[Annotated["{field_input_name_pascal_case}", strawberry.lazy(
        "{schema_app_label}.{api_folder_name}.{module_dir_name}.{field_input_module_dir_name}"
    )]] = strawberry.field(default_factory=list)
"""

TEMPLATE = """
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from typing import TYPE_CHECKING, List, Annotated
from strawberry_django.permissions import (
    IsAuthenticated,
)

from {model_app_label}.models import {model_name}
from {schema_app_label}.{api_folder_name}.filters.{field_node_module_dir_name}

{typechecking_imports}


@strawberry_django.input({model_name})
class {module_class_name}:
    id: auto
{fields}


"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE


    @property
    @cache
    def typechecking_imports(self) -> str:
        imports = []
        for field in self.model._meta.get_fields():
            if field.is_relation:
                field: OneToOneField | ManyToManyField | ForeignKey = field
                imports.append(API_DEPENDANCY_IMPORT.format({
                    "schema_app_label": self.schema_app_label,
                    "api_folder_name": self.api_folder_name,
                    "module_dir_name": self.module_dir_name,
                    "field_input_module_name": snake_case(field.model._meta.model_name, "create_input"),
                    "field_input_name": pascal_case(field.model._meta.model_name, "create_input"),
                }))
        if imports.count() > 0:
            return TYPE_CHECKING_IMPORTS.format(type_checking_imports="\n".join(imports))
        return "\n"

    
    @property
    @cache
    def fields(self) -> str:
        fields_chunks = []
        for field in self.model._meta.get_fields():
            field: Field = field

            if field.is_relation:
                field: OneToOneField | ManyToManyField | ForeignKey = field
                if field.many_to_many or field.one_to_many:
                    field_name = snake_case(field.model._meta.verbose_name_plural, "connection")
                    fields_chunks.append(REL_TO_MANY.format({
                        "field_name": field_name,
                        "schema_app_label": self.schema_app_label,
                        "api_folder_name": self.api_folder_name,
                        "module_dir_name": self.module_dir_name,
                        "field_input_module_name": snake_case(field.model._meta.model_name, "create_input"),
                        "field_input_name": pascal_case(field.model._meta.model_name, "create_input"),
                    }))
                else:
                    fields_chunks.append(REL_TO_ONE.format({
                        "field_name": field.name,
                        "schema_app_label": self.schema_app_label,
                        "api_folder_name": self.api_folder_name,
                        "module_dir_name": self.module_dir_name,
                        "field_input_module_name": snake_case(field.model._meta.model_name, "create_input"),
                        "field_input_name": pascal_case(field.model._meta.model_name, "create_input"),
                    }))
            else:
                fields_chunks.append(FIELD.format({
                    "field_name": field.name
                }))
        
        return "\n".join(fields_chunks)