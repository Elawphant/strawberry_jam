from pathlib import Path
import re
from strawberry_jam.chunks.django_relay.base import indent
from django import apps
from django.core.management.base import CommandError


def extract_docstring_variables(docstring):
    # Regex pattern to match variables inside curly braces
    pattern = r'\{(\w+?)\}'
    # Find all matches
    matches = re.findall(pattern, docstring)
    return matches

def get_attrs(module):
    # Get all attributes of the module
    attributes = dir(module)
    # Filter out built-in attributes
    variables = {attr: getattr(module, attr) for attr in attributes if not attr.startswith('__')}
    return variables


def create_directory(dir_path: Path):
    dir_path.mkdir(parents=True, exist_ok=True)  # Using pathlib

def create_module(filename: str, folder_path: Path, content: str, overwrite=False):
    file_path = Path(folder_path / f"{filename}.py")
    if not file_path.exists() or overwrite == True:
        with open(file_path, 'w') as file:
            file.write(content)


def pascal_case(text: str):
    text = re.sub(r"(_|-)+", " ", snake_case(str(text)))
    words = str(text).split(" ")
    # Concatenate words
    return "".join([word.title() for word in words])

def snake_case(text):
    # Handle camelCase, kebab-case, and PascalCase
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(text))
    text = re.sub(r"[-\s]", "_", str(text))
    # Convert to lowercase and remove consecutive underscores
    return re.sub(r"_{2,}", "_", str(text)).lower()


def name_class(typename: str, prefix: str = "", suffix:str = ""):
    return f"{pascal_case(prefix)}{pascal_case(typename)}{pascal_case(suffix)}"


def name_module(typename: str, prefix: str = "", suffix:str = ""):
    return snake_case(f"{str(prefix) + '_' if prefix else ''}{str(typename)}_{str(suffix)}")


def append_chunk(content: str, chunk:str, variables: dict, indentation_level: int = 0):
    attrs = extract_docstring_variables(chunk)
    chunk_kwargs = {attr: variables.get(attr) for attr in attrs}
    content += f"{indent * indentation_level if indentation_level > 0 else ''}" + chunk.format(**chunk_kwargs) + "\n"


def validate_model(options):
    model = options["model"]
    [app_label, modelname] = model.split(".")
    schema_app = options["schema_app"]

    try:
        apps.get_app_config(app_label)
        apps.get_app_config(schema_app)
    except (LookupError, ImportError) as e:
        raise CommandError(
            f"{e}. Are you sure your INSTALLED_APPS setting is correct?"
        )
    try:
        model = apps.get_model(app_label, modelname)
    except LookupError as e:
        raise CommandError(e)
