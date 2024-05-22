from strawberry_jam.jam import StrawberryJamTemplate
from functools import cache

TEMPLATE = """
# TODO: Strawberry-Jam: review this file
from strawberry_jam.forms import ModelForm
from {model_app_label}.models import {model_name}


class {module_class_name}(ModelForm):
    class Meta:
        model = {model_name}
        fields = [{fields}]

"""

class Template(StrawberryJamTemplate):
    template: str = TEMPLATE    

    @property
    @cache
    def fields(self) -> str:
        return ", ".join([field.name for field in self.model._meta.get_fields()])

