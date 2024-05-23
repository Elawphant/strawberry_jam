from django.forms import ModelForm
from strawberry_jam.utils import snake_case
import re
from typing import Dict, Any



class ModelForm(ModelForm):

    class Meta:
        abstract = True

    def validate(self, data):
        check_add_remove_conflict(data, self)
        error_fields_to_replace = set()

        for field_name, field_value in data.items():
            if field_name.startswith('add_to_'):
                name = snake_case(field_name)[len("add_to_"):][:"_connection"]
                data[name] = data.get(name, set()).union(set(field_value))
                data.pop(field_name)
                error_fields_to_replace.add(name)
            elif field_name.startswith('remove_from_'):
                name = snake_case(field_name)[len("remove_from_"):][:"_connection"]
                data[name] = data.get(name, set()).difference(set(field_value))
                data.pop(field_name)
                error_fields_to_replace.add(name)

        super().validate(data.copy())
        # If super().validate will raise an error on the to-many relation, 
        # we need to change the error field name to the add_to_{fieldname}_connection.
        # it is ok to ignore remove_from type fields, because they will not raise errors here
        for field_name in error_fields_to_replace:
            if self.errors.get(field_name):
                self.errors[f"add_to_{field_name}_connection"] = self.errors.get(field_name)
                self.errors.pop(field_name)


def check_add_remove_conflict(data: Dict[str, Any], form: ModelForm) -> None:
    tracked_ids = {}

    # Populate the dictionary with sets of IDs for each unique suffix, distinguishing add and remove
    for key, value in data.items():
        match = re.match(r'^(add_to_|remove_from_)(.+)$', key)
        if match:
            action, suffix = match.groups()
            if suffix not in tracked_ids:
                tracked_ids[suffix] = {'add': set(), 'remove': set()}
            if action == 'add_to_':
                tracked_ids[suffix]['add'].update(value)
            elif action == 'remove_from_':
                tracked_ids[suffix]['remove'].update(value)

    # Check for conflicts in each suffix and add errors to the form
    for suffix, ids in tracked_ids.items():
        conflict_ids = ids['add'].intersection(ids['remove'])
        if conflict_ids:
            error_msg = f"Conflicting IDs in add_to_{suffix} and remove_from_{suffix}: {conflict_ids}"
            form.add_error(None, error_msg)