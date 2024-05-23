from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.utils import create_module, get_modules_and_classes, snake_case
from pathlib import Path

DEPENDENCY_IMPORT = """"
from {schema_app_label}.{api_folder_name}.queries.{query_module_name} import {query_class_name} \n
"""

TEMPLATE = """
import strawberry
{dependency_imports}

@strawberry.type
class Query(
{queries_list}
    ):
    pass
    
@strawberry.type
class Mutation(
{mutations_list}
    ):
    pass
    
schema = strawberry.Schema(query=Query, mutation=Mutation)

"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE

    overwrite: bool = True  

    query_class_names: list[str] = []

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

    @property
    @cache
    def queries(self):
        dir = self.api_folder_path / Path("queries")
        return get_modules_and_classes(dir)

    @property
    @cache
    def mutations(self):
        dir = self.api_folder_path / Path("mutations")
        return get_modules_and_classes(dir)

    @property
    @cache
    def dependency_imports(self) -> str:
        content = []
        for query_module_name, query_class_name in {*self.queries, *self.mutations}:
            content.append(DEPENDENCY_IMPORT.format({
                "schema_app_label": self.schema_app_label,
                "api_folder_name": self.api_folder_name,
                "query_module_name": query_module_name,
                "query_class_name": query_class_name,
            }))
        return "".join(content)
    
    @property
    @cache
    def queries_list(self) -> str:
        return ",\n".join(self.queries.values())
    @property
    @cache
    def mutations_list(self) -> str:
        return ",\n".join(self.mutations.values())



    def generate_module(self) -> None:
        context = {}
        for var_name in self.template_variables:
            assert isinstance(getattr(self, var_name), str), "All values for template variables must be string" 
            context[var_name] = getattr(self, var_name)

        content = self.template.format(**context)
        create_module("schema", self.api_folder_path, content, self.overwrite)
