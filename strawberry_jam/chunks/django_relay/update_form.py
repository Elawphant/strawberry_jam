imports = """
from strawberry_jam import ModelForm
"""


type_class = """
class {update_form_name_pascal_case}(ModelForm):
    class Meta:
        model = {model_name_pascal_case}
        fields = [id, {model_fields_list}]
"""