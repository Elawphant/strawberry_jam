from django.forms import ModelForm
from strawberry_jam.queryset import QuerySetManager
import re
from typing import Dict, Any


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





class ModelForm(ModelForm):
    class Meta:
        abstract = True
        queryset_manager: QuerySetManager

    def __init__(self, info, data, *args, **kwargs) -> None:
        self.info = info
        super().__init__(data, *args, **kwargs)

    def validate(self, data):
        check_add_remove_conflict(data, self)
        return super().validate(data)
    
    def get_queryset(self):
        return self.Meta.queryset_manager.get_queryset(self.info)
    
    def clean(self):
        cleaned_data = {**super().clean()}
        modified_cleaned_data = {}

        for field_name, value in cleaned_data.items():
            match = re.match(r'^(add_to_|remove_from_)(.+)$', field_name)
            if match:
                action, suffix = match.groups()
                related_field_name = f"{suffix}_set"
                if related_field_name not in self.instance.__dict__:
                    self.add_error(None, f"Invalid related field: {related_field_name}")
                    continue
                if action == 'add_to_':
                    modified_cleaned_data[related_field_name] = value
                elif action == 'remove_from_':
                    modified_cleaned_data[related_field_name] = [id for id in getattr(self.instance, related_field_name).all() if id not in value]
                cleaned_data.pop(field_name)
        
        return {**cleaned_data, **modified_cleaned_data}

