from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.codegen.utils import pascal_case, snake_case
from django.db.models import Field, OneToOneField, ManyToManyField, ForeignKey

TEMPLATE = """
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto
from typing import TYPE_CHECKING, List, Annotated

from {model_app_label}.models import {model_name}

@strawberry_django.filter({model_name}, lookups=True)
class {module_class_name}:
    id: auto
{fields}
"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE    
    
    @property
    @cache
    def fields(self) -> str:
        fields_chunks = []
        for field in self.model._meta.get_fields():
            field: Field = field
            if field.is_relation and (field.many_to_many or field.many_to_one): 
                fields_chunks.append(f"    {snake_case(field.model._meta.verbose_name_plural, "connection")}: auto\n")
            else: 
                fields_chunks.append(f"    {field.name}: auto\n")

        return "\n".join(fields_chunks)