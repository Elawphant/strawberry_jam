
from codegen import defaults
from codegen.utils import (
    create_module,
    snake_case,
    name_class,
    append_chunk
)

from pathlib import Path
from django.apps import apps
from django.db.models import OneToOneField, ManyToManyField, ForeignKey

from django_relay import (
    base, 
    node, 
    filter, 
    order, 
    query, 
    create_input, 
    update_input, 
    create_form, 
    update_form, 
    mutation,
    urls,
    schema
)
import textwrap
from typing import TypedDict
import importlib
import inspect
import strawberry

module_types = [i["name"] for i in defaults.module_types.values()]


base_output = f"""
{base.todo_comments}
{base.imports}
"""

class Options(TypedDict):
    schema_app_label: str
    api_folder_name: str
    model_app_label: str
    model_name_pascal_case: str
    overwrite: bool | None

def gen_folder_structure(schema_app_label: str, api_folder_name: str):
    modules = list(set(i["dependency_folder_snake_case"] for i in defaults.module_types.values()))
    app_folder = Path(schema_app_label / api_folder_name)
    create_module("__init__", app_folder)
    for module_name in modules:
        module_folder = Path(schema_app_label / api_folder_name / module_name)
        create_module("__init__", module_folder, "", False)

    urls_content = append_chunk("", urls.output, {
        "schema_app_label": schema_app_label,
        "api_folder_name": api_folder_name
    })
    create_module("urls", app_folder, urls_content) 



def get_strawberry_type_name(module: object):
    # Iterate over attributes of the module
    for name, obj in inspect.getmembers(module):
        # Check if the attribute is a class and is a subclass of strawberry.type
        if inspect.isclass(obj) and hasattr(obj, "_type_definition"):
            return obj.__name__



def process_schema(schema_app_label: str, api_folder_name: str): 
    outputs = {
        "queries": set(),
        "mutations": set(),
    }
    imports = """"""

    for key in list(outputs.keys()):
        dir = Path(schema_app_label / api_folder_name / key)
        for file in dir.glob('*.py'):
            module_name = f"{schema_app_label}.{api_folder_name}.{dir}.{file.stem}"
            # Import the module
            module = importlib.import_module(module_name)
            type_name = get_strawberry_type_name(module)
            outputs.get(key).add(type_name)

            append_chunk(imports, textwrap.dedent(base.api_dependency_import), {
                "schema_app_label": schema_app_label,
                "api_folder_name": api_folder_name,
                "dependency_package_name_snake_case": module_name,
                "dependency_name_snake_case": module_name,
                "dependency_name_pascal_case": type_name
            })
    

    content = """"""
    append_chunk("", schema.output, {
        "comma_separated_list_of_pascal_case_query_names": outputs.get("queries").join(", "),
        "comma_separated_list_of_pascal_case_mutation_names": outputs.get("mutations").join(", "),
        "dependency_imports": imports
    })
    create_module("schema", Path(schema_app_label / api_folder_name), content, True)



def process(options: Options) -> None:
    DEFAULTS = defaults.module_types
    NODE = DEFAULTS.get("node")
    FILTER = DEFAULTS.get("filter")
    ORDER = DEFAULTS.get("order")
    CR_FORM = DEFAULTS.get("create_form")
    UP_FORM = DEFAULTS.get("update_form")
    CR_INPUT = DEFAULTS.get("create_input")
    UP_INPUT = DEFAULTS.get("update_input")
    QUERY = DEFAULTS.get("query")
    MUTATION = DEFAULTS.get("mutation")

    # the app where to generate modules
    schema_app_label: str = options.get("schema_app_label")
    # the name of the folder where all modules will reside
    api_folder_name: str = options.get("api_folder_name", defaults.API_FOLDER_NAME)
    # the app_label of the model the modules are being generated for
    model_app_label: str = options.get("model_app_label")
    # the model the modules are being generated for
    model_name_pascal_case: str = options.get("model_name")

    # node
    node_name_pascal_case: str = name_class(model_name_pascal_case, "", NODE.get("name"))
    node_name_snake_case: str = snake_case(node_name_pascal_case)

    # filter
    filter_name_pascal_case: str = name_class(model_name_pascal_case, "", FILTER.get("name"))
    filter_name_snake_case: str = snake_case(filter_name_pascal_case)

    # form
    create_form_name_pascal_case: str = name_class(model_name_pascal_case, "", CR_FORM.get("name"))
    update_form_name_pascal_case: str = name_class(model_name_pascal_case, "", UP_FORM.get("name"))
    create_form_name_snake_case: str = snake_case(create_form_name_pascal_case)
    update_form_name_snake_case: str = snake_case(update_form_name_pascal_case)

    # ordering
    order_name_pascal_case: str = name_class(model_name_pascal_case, "", ORDER.get("name"))
    order_name_snake_case: str = snake_case(order_name_pascal_case)

    # inputs
    create_input_name_pascal_case: str = name_class(model_name_pascal_case, "", CR_INPUT.get("name"))
    update_input_name_pascal_case: str = name_class(model_name_pascal_case, "", UP_INPUT.get("name"))
    create_input_name_snake_case: str = snake_case(create_input_name_pascal_case)
    update_input_name_snake_case: str = snake_case(update_input_name_pascal_case)

    # query 
    query_name_pascal_case = name_class(model_name_pascal_case, "", QUERY.get("name"))
    query_name_snake_case = snake_case(query_name_pascal_case)

    # mutation
    mutation_name_pascal_case = name_class(model_name_pascal_case, "", MUTATION.get("name"))
    mutation_name_snake_case = snake_case(mutation_name_pascal_case)

    variables = { 
        "schema_app_label": schema_app_label,
        "api_folder_name": api_folder_name,
        "model_app_label": model_app_label,
        "model_name_pascal_case": model_name_pascal_case,
        "node_name_pascal_case": node_name_pascal_case,
        "node_name_snake_case": node_name_snake_case,
        "filter_name_pascal_case": filter_name_pascal_case,
        "filter_name_snake_case": filter_name_snake_case,
        "create_form_name_pascal_case": create_form_name_pascal_case,
        "update_form_name_pascal_case": update_form_name_pascal_case,
        "create_form_name_snake_case": create_form_name_snake_case,
        "update_form_name_snake_case": update_form_name_snake_case,
        "order_name_pascal_case": order_name_pascal_case,
        "order_name_snake_case": order_name_snake_case,
        "create_input_name_pascal_case": create_input_name_pascal_case,
        "update_input_name_pascal_case": update_input_name_pascal_case,
        "create_input_name_snake_case": create_input_name_snake_case,
        "update_input_name_snake_case": update_input_name_snake_case,
        "query_name_pascal_case": query_name_pascal_case,
        "query_name_snake_case": query_name_snake_case,
        "mutation_name_pascal_case": mutation_name_pascal_case,
        "mutation_name_snake_case": mutation_name_snake_case
    }
    # generate folder structure
    gen_folder_structure(schema_app_label=schema_app_label, api_folder_name=api_folder_name)


    outputs = { name: """""" for name in module_types}
    type_checking_imports = {
        name: """""" for name in module_types
    }    

    main_model = apps.get_model(model_app_label, model_name_pascal_case)
    # node
    for chunk in [base_output, base.type_checking, node.imports, node.type_class]:
        append_chunk(outputs.get("node"), chunk, variables)
        append_chunk(type_checking_imports.get("node"), base.model_import, variables)

    # filter
    for chunk in [base_output, base.type_checking, filter.type_class]:
        append_chunk(outputs.get("filter"), chunk, variables)

    # order
    for chunk in [base_output, order.type_class]:
        append_chunk(outputs.get("filter"), chunk, variables)

    # create input
    for chunk in [base_output, create_input.type_class]:
        append_chunk(outputs.get("create_input"), chunk, variables)

    # update input
    for chunk in [base_output, update_input.type_class]:
        append_chunk(outputs.get("update_input"), chunk, variables)

    # forms
    # textwrap.dedent model import because no import conflict is expected
    for chunk in [base_output, create_form.imports, textwrap.dedent(base.model_import), create_form.type_class]:
        append_chunk(outputs.get("update_form"), chunk, variables)
    for chunk in [base_output, update_form.imports, textwrap.dedent(base.model_import), create_form.type_class]:
        append_chunk(outputs.get("update_form"), chunk, variables)

    # query
    for chunk in [base_output, query.type_class]:
        append_chunk(outputs.get("query"), chunk, variables)
    append_chunk(outputs.get("query"), query.field, variables)

    # mutation
    append_chunk(outputs.get("mutation"), base_output, variables)
    append_chunk(outputs.get("mutation"), textwrap.dedent(base.api_dependency_import), {
        "schema_app_label": schema_app_label,
        "dependency_folder_snake_case": CR_FORM.get("dependency_folder_snake_case"),
        "dependency_name_pascal_case": create_form_name_pascal_case,
        "dependency_name_snake_case": create_form_name_snake_case
    })
    append_chunk(type_checking_imports.get("mutation"), textwrap.dedent(base.api_dependency_import), {
        "schema_app_label": schema_app_label,
        "dependency_folder_snake_case": UP_FORM.get("dependency_folder_snake_case"),
        "dependency_name_pascal_case": update_form_name_pascal_case,
        "dependency_name_snake_case": update_form_name_snake_case
    })
    append_chunk(outputs.get("mutation"), mutation.type_class, variables)

    form_fields: list[str] = []

    # fields and relations related chunks
    for field in main_model._meta.get_fields():
        if field.name is not "id":
            form_fields.append(field.name)

        if field.is_relation:
            field: OneToOneField | ManyToManyField | ForeignKey = field
            
            # TYPE_CHECKING imports
            # node
            field_node_name_pascal_case = name_class(field.model._meta.model_name, "", NODE.get("name"))
            append_chunk(type_checking_imports.get(NODE.get("name")), base.model_import, {
                "model_app_label": field.model._meta.app_label,
                "model_name_pascal_case": field.model._meta.model_name
            })

            # filter
            field_filter_name_pascal_case = name_class(field.model._meta.model_name, "", FILTER.get("name"))
            append_chunk(type_checking_imports.get(FILTER.get("name")), base.api_dependency_import, {
                "schema_app_label": schema_app_label,
                "dependency_folder_snake_case": FILTER.get("dependency_folder_snake_case"),
                "dependency_name_pascal_case": field_filter_name_pascal_case,
                "dependency_name_snake_case": snake_case(field_filter_name_pascal_case),
            })

            # ordering field related imports
            field_order_name_pascal_case = name_class(field.model._meta.model_name, "", ORDER.get("name"))
            append_chunk(type_checking_imports.get(ORDER.get("name")), base.api_dependency_import, {
                "schema_app_label": schema_app_label,
                "dependency_folder_snake_case": ORDER.get("dependency_folder_snake_case"),
                "dependency_name_pascal_case": field_order_name_pascal_case,
                "dependency_name_snake_case": snake_case(field_order_name_pascal_case),
            })

            # input 
            for INPUT in [DEFAULTS.get("create_input"), DEFAULTS.get("update_input")]:
                field_input_name_pascal_case = name_class(field.model._meta.model_name, "", INPUT.get("name"))
                append_chunk(type_checking_imports.get(INPUT.get("name")), base.api_dependency_import, {
                    "schema_app_label": schema_app_label,
                    "dependency_folder_snake_case": INPUT.get("dependency_folder_snake_case"),
                    "dependency_name_pascal_case": field_input_name_pascal_case,
                    "dependency_name_snake_case": snake_case(field_input_name_pascal_case),
                })

            # fields   
            if field.many_to_many or field.one_to_many:
                field_name = snake_case(field.name) + "_connection"
                field_vars = {
                    **variables,
                    "field_name_snake_case": field_name,
                    "field_node_name_pascal_case": field_node_name_pascal_case,
                    "field_node_name_snake_case": snake_case(field_node_name_pascal_case)
                }

                append_chunk(outputs.get("node"), node.relation_to_many, {
                    **field_vars,
                })
                append_chunk(outputs.get("filter"), filter.relation_to_many, {
                    **field_vars,
                })
                append_chunk(outputs.get("order"), order.relation_to_many, {
                    **field_vars,
                })
                append_chunk(outputs.get("create_input"), create_input.relation_to_many, {
                    **field_vars,
                })
                append_chunk(outputs.get("update_input"), update_input.relation_to_many, {
                    **field_vars,
                })
                
            else:
                append_chunk(outputs.get("node"), node.relation_to_one, field_vars)
                append_chunk(outputs.get("filter"), filter.relation_to_one, field_vars)
                append_chunk(outputs.get("order"), order.relation_to_one, field_vars)
                append_chunk(outputs.get("input"), create_input.relation_to_one, field_vars)
                append_chunk(outputs.get("input"), update_input.relation_to_one, field_vars)
        else:
            append_chunk(outputs.get("node"), node.field, field_vars)
            append_chunk(outputs.get("filter"), filter.field, field_vars)
            append_chunk(outputs.get("order"), order.field, field_vars)
            append_chunk(outputs.get("input"), create_input.field, field_vars)
            append_chunk(outputs.get("input"), update_input.field, field_vars)
        
        # format entire contents for type_checking imports
        [value.format(type_checking_imports=type_checking_imports.get(key)) for key, value in outputs.items()]
        [value.format(model_fields_list=form_fields.join(",")) for key, value in outputs.items() if key in ["create_form", "update_form"]]
        
    for key, content in outputs.items():
        create_module(
            snake_case(variables.get(f"{key}_name_snake_case"), 
            DEFAULTS.get(key).get("dependency_folder_snake_case")),
            content,
            options.get("overwrite", False)
        )

    # urls 
    url_content = """"""
    append_chunk(url_content, urls.output, {
        "schema_app_label": schema_app_label, 
        "api_folder_name": api_folder_name,
    })

    create_module("urls", Path(schema_app_label / api_folder_name), url_content, False)

    # collect all schema
    process_schema(schema_app_label, api_folder_name)