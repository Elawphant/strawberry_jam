from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.utils import pascal_case, snake_case, conv

TEMPLATE = """
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django
from {schema_app_label}.{api_folder_name}.nodes.{node_module_name} import {node_class_name}

@strawberry.type(name="Query")
class {module_class_name}:
    {field_name}: strawberry_django.relay.ListConnectionWithTotalCount[{node_class_name}] = strawberry_django.connection()
"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE    


    @property
    @cache
    def node_class_name(self):
        return pascal_case(self.model_name, conv("NODE_SUFFIX"))


    @property
    @cache
    def node_module_name(self):
        return snake_case(self.model_name, conv("NODE_SUFFIX"))
    
    @property
    @cache
    def field_name(self):
        return snake_case(self.model._meta.verbose_name_plural, conv("CONNECTION_SUFFIX"))
    