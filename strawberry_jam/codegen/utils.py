from pathlib import Path
import re
from django.apps import apps
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


def pascal_case(**chunks: list[str]) -> str:
    """
    Returns a pascal case string made from the supplied arguments
    """
    assert chunks.__len__() > 0, f"At least one string argument must be passed to 'pascal_case'"
    assert all(isinstance(ch, str) for ch in chunks) > 0, f"All arguments passed to 'pascal_case' must be string"
    pascal_case_chunks = []
    for ch in chunks:
        ch = re.sub(r"(_|-)+", " ", snake_case(str(ch))), 
        words = str(ch).split(" ")
        pascal_case_chunks = [*pascal_case_chunks, word.title() for word in words]
    return "".join(pascal_case_chunks)

def snake_case(**chunks:list[str]) -> str:
    """
    Returns a snake case string made from the supplied arguments
    """
    assert chunks.__len__() > 0, f"At least one string argument must be passed to 'snake_case'"
    assert all(isinstance(ch, str) for ch in chunks) > 0, f"All arguments passed to 'snake_case' must be string"
    snake_cased_chunks = []
    for ch in chunks:
        # Handle camelCase, kebab-case, and PascalCase
        ch = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(ch))
        ch = re.sub(r"[-\s]", "_", str(ch))
        # Convert to lowercase and remove consecutive underscores
        snake_cased_chunks.append(re.sub(r"_{2,}", "_", str(ch)).lower())
    return "_".join(snake_cased_chunks)


def name_class(typename: str, prefix: str = "", suffix:str = ""):
    return f"{pascal_case(prefix)}{pascal_case(typename)}{pascal_case(suffix)}"


def name_module(typename: str, prefix: str = "", suffix:str = ""):
    return snake_case(f"{str(prefix) + '_' if prefix else ''}{str(typename)}_{str(suffix)}")


def append_chunk(content: str, chunk:str, variables: dict, indentation_level: int = 0):
    print(f"Processing chunk: {chunk}")  # Debug: Show chunk before processing
    attrs = extract_docstring_variables(chunk)
    print(f"Extracted attributes: {attrs}")  # Debug: Show extracted attributes
    chunk_kwargs = {attr: variables.get(attr) for attr in attrs}
    print(f"Chunk kwargs: {chunk_kwargs}")  # Debug: Show chunk keyword arguments
    indentation = '    ' * 4 * indentation_level if indentation_level > 0 else ''
    formatted_chunk = format(chunk, chunk_kwargs)
    print(f"Formatted chunk: {formatted_chunk}")  # Debug: Show formatted chunk
    return content + indentation + formatted_chunk + "\n"


def format(text, variables: dict):
    def replace_with_value(match):
        var_name = match.group(1)
        return str(variables.get(var_name, f"{{{var_name}}}"))  # Return default if unmatched

    return re.sub(r"{([a-zA-Z_][a-zA-Z0-9_]*)}", replace_with_value, text)


def validate_model(options):
    app_label = options.get("model_app_label")
    modelname = options.get("model_name_pascal_case")
    schema_app = options.get("schema_app_label")

    try:
        apps.get_app_config(app_label)
        apps.get_app_config(schema_app)
    except (LookupError, ImportError) as e:
        raise CommandError(f"Error validating apps: {e}")
    try:
        apps.get_model(app_label, modelname)
    except LookupError as e:
        raise CommandError(f"Error validating models: {e}")
