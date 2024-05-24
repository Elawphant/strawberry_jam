from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache
from strawberry_jam.utils import snake_case, pascal_case


REL_TO_ONE = """
        self.{field_name} = forms.ModelChoiceField(queryset={field_queryset_manager_name}.get_queryset(self.info))
"""

REL_TO_MANY = """
        self.{field_name} = forms.ModelMultipleChoiceField(queryset={field_queryset_manager_name}.get_queryset(self.info), required={field_is_required})
"""

FIELD_QS_MANAGER_IMPORT = """
from {schema_app_label}.{api_folder_name}.query_set_managers.{field_queryset_manager_module_name} import {field_queryset_manager_name}
"""

TEMPLATE = """
# TODO: Strawberry-Jam: review this file
from django import forms
from strawberry_jam.forms import ModelForm
from {model_app_label}.models import {model_name}
from {schema_app_label}.{api_folder_name}.nodes.{node_module_name} import {node_name}
from {schema_app_label}.{api_folder_name}.query_set_managers.{queryset_manager_module_name} import {queryset_manager_name}

{field_query_set_manager_imports}

class {module_class_name}(ModelForm):

    def __init__(self, info, data, *args, **kwargs) -> None:
        {rel_fields}
        super().__init__(info, data, *args, **kwargs)


    class Meta:
        model = {model_name}
        fields = [{field_names}]
        queryset_manager = {queryset_manager_name}

"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE    

    @property
    @cache
    def field_names(self) -> str:
        fields = []
        for field in self.model._meta.get_fields():
            if field.is_relation:
                # fields.append(snake_case("add_to", field.name, "connection"))
                # fields.append(snake_case("remove_from", field.name, "connection"))
                pass
            else:
                fields.append(field.name)
        return ", ".join([f"'{f}'" for f in fields if f != "id"])

    @property
    @cache
    def rel_fields(self) -> str:
        rel_fields = []
        for field in self.model._meta.get_fields():
            if field.is_relation:
                if field.one_to_many or field.many_to_many:
                    rel_fields.append(REL_TO_MANY.format(**{
                        "field_name": snake_case("add_to", field.name, "connection"),
                        "field_queryset_manager_name": pascal_case(field.remote_field.model.__name__, "query_set_manager"),
                        "field_is_required": not field.null,
                    }))
                    rel_fields.append(REL_TO_MANY.format(**{
                        "field_name": snake_case("remove_from", field.name, "connection"),
                        "field_queryset_manager_name": pascal_case(field.remote_field.model.__name__, "query_set_manager"),
                        "field_is_required": not field.null,
                    }))
                else:
                    rel_fields.append(REL_TO_ONE.format(**{
                        "field_name": field.name,
                        "field_queryset_manager_name": pascal_case(field.remote_field.model.__name__, "query_set_manager"),
                        "field_is_required": not field.null,
                    }))
        return "".join(rel_fields)


    @property
    @cache
    def node_module_name(self):
        return snake_case(self.model_name, "node")
    
    @property
    @cache
    def node_name(self):
        return pascal_case(self.model_name, "node")
    
    @property
    @cache
    def queryset_manager_name(self):
        return pascal_case(self.model_name, "query_set_manager")
    
    @property
    @cache
    def queryset_manager_module_name(self):
        return snake_case(self.model_name, "query_set_manager")
    

    @property
    @cache
    def field_query_set_manager_imports(self):
        qs_imports = []
        for field in self.model._meta.get_fields():
            if field.is_relation:
                qs_imports.append(FIELD_QS_MANAGER_IMPORT.format(**{
                    "schema_app_label": self.schema_app_label,
                    "api_folder_name": self.api_folder_name,
                    "field_queryset_manager_name": pascal_case(field.remote_field.model.__name__, "query_set_manager"),
                    "field_queryset_manager_module_name": snake_case(field.remote_field.model.__name__, "query_set_manager"),
                }))
        return "".join(qs_imports)
