from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.utils import snake_case
from django.db.models import Field
TEMPLATE = """
# TODO: Strawberry-Jam: review this file
import strawberry_django
from strawberry import auto

from {model_app_label}.models import {model_name}

@strawberry_django.filter({model_name}, lookups=True)
class {module_class_name}:
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
                fields_chunks.append(f"    {snake_case(field.model._meta.verbose_name_plural, "connection")}: auto")
            else: 
                fields_chunks.append(f"    {field.name}: auto")

        return "\n".join(fields_chunks)