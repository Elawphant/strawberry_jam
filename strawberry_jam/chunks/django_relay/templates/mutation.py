from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.codegen.utils import pascal_case, snake_case


TEMPLATE = """
# TODO: Strawberry-Jam: review this file
import strawberry
import strawberry_django

from {schema_app_label}.{api_folder_name}.{module_dir_name}.nodes.{node_module_name} import {node_class_name}
from {schema_app_label}.{api_folder_name}.{module_dir_name}.inputs.{create_input_module_name} import {create_input_class_name}
from {schema_app_label}.{api_folder_name}.{module_dir_name}.inputs.{update_input_module_name} import {update_input_class_name}
from {schema_app_label}.{api_folder_name}.{module_dir_name}.forms.{create_form_module_name} import {create_form_class_name}
from {schema_app_label}.{api_folder_name}.{module_dir_name}.forms.{update_form_module_name} import {update_form_class_name}

@strawberry.type(name="Mutation")
class {module_class_name}:
    @strawberry_django.mutation(handle_django_errors=True)
    def create_{field_name}(self, data: {input_class_name}):
        form = {create_form_class_name}(data)
        return cast({node_class_name}, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_{field_name}(self, data: {input_class_name}):
        form = {update_form_class_name}(data)
        return cast({node_class_name}, form.save())

    delete_{field_name}: {node_class_name} = strawberry_django.mutations.delete(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE    

    @property
    @cache
    def field_name(self) -> str:
        return self.model_name

    @property
    @cache
    def node_module_name(self):
        return snake_case(self.model_name, "node")
    
    @property
    @cache
    def node_class_name(self):
        return pascal_case(self.model_name, "node")
    
    @property
    @cache
    def create_input_module_name(self):
        return snake_case(self.model_name, "create_input")
    
    @property
    @cache
    def create_input_class_name(self):
        return pascal_case(self.model_name, "create_input")

    @property
    @cache
    def create_form_module_name(self):
        return snake_case(self.model_name, "update_form")

    @property
    @cache
    def create_form_class_name(self):
        return pascal_case(self.model_name, "create_form")


    @property
    @cache
    def update_input_module_name(self):
        return snake_case(self.model_name, "update_input")
    
    @property
    @cache
    def update_input_class_name(self):
        return pascal_case(self.model_name, "update_input")
    
    @property
    @cache
    def update_form_module_name(self):
        return snake_case(self.model_name, "update_form")
    
    @property
    @cache
    def update_form_class_name(self):
        return pascal_case(self.model_name, "update_form")

    