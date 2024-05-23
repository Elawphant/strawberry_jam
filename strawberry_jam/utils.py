from pathlib import Path
import re, inspect
from django.apps import apps
from django.core.management.base import CommandError
from importlib import import_module


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


def pascal_case(*chunks: list[str]) -> str:
    """
    Returns a pascal case string made from the supplied arguments
    """
    assert chunks.__len__() > 0, f"At least one string argument must be passed to 'pascal_case'"
    chunks = [str(ch) for ch in chunks]
    pascal_case_chunks = []
    for ch in chunks:
        ch = re.sub(r"(_|-)+", " ", snake_case(ch))
        words = ch.split(" ")
        pascal_case_chunks = [*pascal_case_chunks, *[word.title() for word in words]]
    return "".join(pascal_case_chunks)

def snake_case(*chunks: list[str]) -> str:
    """
    Returns a snake case string made from the supplied arguments
    """
    assert chunks.__len__() > 0, f"At least one string argument must be passed to 'snake_case'"
    chunks = [str(ch) for ch in chunks]
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
    attrs = extract_docstring_variables(chunk)
    chunk_kwargs = {attr: variables.get(attr) for attr in attrs}
    indentation = '    ' * 4 * indentation_level if indentation_level > 0 else ''
    formatted_chunk = format(chunk, chunk_kwargs)
    return content + indentation + formatted_chunk + "\n"


def format(text, variables: dict):
    def replace_with_value(match):
        var_name = match.group(1)
        return str(variables.get(var_name, f"{{{var_name}}}"))  # Return default if unmatched

    return re.sub(r"{([a-zA-Z_][a-zA-Z0-9_]*)}", replace_with_value, text)


def validate_model(options):
    app_label = options.get("model_app_label")
    modelname = options.get("model_name")
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


def get_query_and_mutation_types(module: object):
    for name, obj in inspect.getmembers_static(module):
        # Check if the attribute is a class and is a subclass of strawberry.type
        if inspect.isclass(obj) and ("Query" in name or "Mutation" in name):
            return name
        return None
    

def get_modules_and_classes(dir: Path) -> dict[str, str]:
    assert dir.is_dir(), f"Provided path '{dir}' is not a directory."

    output: dict[str, str] = {}

    for file in dir.glob('*.py'):
        module_name = file.stem
        # Import the module
        try:
            module = import_module(f"{dir.name}.{module_name}")
            if module:
                type_name = get_query_and_mutation_types(module)
                if type_name:
                    output[module_name] = type_name
        except:
            pass
    return output


def process_template(options: dict, flavor: str):
    dir = Path(f"strawberry_jam/chunks/{flavor}/templates")
    assert dir.is_dir(), f"Provided path '{dir}' is not a directory."
    for file in [file for file in dir.glob('*.py') if file.stem not in ["__init__", "urls", "schema"]]:
        module = import_module(f"{str(dir).replace("/", ".")}.{file.stem}")
        template_class = module.Template  # Access class at module level
        template_class(options).generate_module()

def finalize_schema(options: dict, flavor: str):
    dir = Path(f"strawberry_jam/chunks/{flavor}/templates")
    assert dir.is_dir(), f"Provided path '{dir}' is not a directory."
    for file in [file for file in dir.glob('*.py') if file.stem in ["urls", "schema"]]:
        module = import_module(f"{str(dir).replace("/", ".")}.{file.stem}")
        template_class = module.Template  # Access class at module level
        template_class(options).generate_module()
