import importlib

from .defaults import (
    NODE,
    CONNECTION,
    FILTER,
    ORDER,
    QUERY,
    INPUT,
    MUTATION,
)
from utils import (
    create_directory,
    create_module,
    pascal_case,
    snake_case,
    name_class,
    name_module,
    extract_docstring_variables,
    get_chunks
)

module_names = [
    "filter",
    "globals",
    "input",
    "mutation",
    "node",
    "order",
    "query",
]



def process(flavor_name: str, options: dict):
    flavor = {}
    for module_name in module_names:
        flavor[module_name] = get_chunks(importlib.import_module(f"..chunks.{flavor_name}.{module_name}"))

    # schema_app_label

    # for key, chunks in flavor.items():

