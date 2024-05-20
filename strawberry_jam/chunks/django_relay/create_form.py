imports = """
from strawberry_jam import ModelForm
"""


type_class = """
class {create_form_name_pascal_case}(ModelForm):
    class Meta:
        model = {model_name_pascal_case}
        fields = [{model_fields_list}]

"""