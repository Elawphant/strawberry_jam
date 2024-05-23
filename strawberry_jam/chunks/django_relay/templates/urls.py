
from strawberry_jam.jam import StrawberryJamTemplate
from strawberry_jam.utils import create_module, snake_case
from functools import cache

TEMPLATE = """
from django.urls import path
from strawberry.django.views import GraphQLView

from {schema_app_label}.{api_folder_name}.schema import schema

urlpatterns = [
    path('graphql', GraphQLView.as_view(schema=schema)),
]
"""


class Template(StrawberryJamTemplate):
    template: str = TEMPLATE

    @property
    @cache
    def module_name(self) -> str:
        return snake_case(self.__module__.split(".")[-1])
    
    @property
    @cache
    def module_dir_name(self):
        return self.api_folder_name

    def validate_options(self, options: dict):
        return 

    def generate_module(self):
        context = {}
        for var_name in self.template_variables:
            assert isinstance(getattr(self, var_name), str), "All values for template variables must be string" 
            context[var_name] = getattr(self, var_name)

        content = self.template.format(**context)
        create_module("urls", self.api_folder_path, content, self.overwrite)

    def generate_module(self):
        context = {}
        for var_name in self.template_variables:
            assert isinstance(getattr(self, var_name), str), "All values for template variables must be string" 
            context[var_name] = getattr(self, var_name)

        content = self.template.format(**context)
        create_module("urls", self.api_folder_path, content, self.overwrite)
