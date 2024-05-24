

from django.db.models import Model, QuerySet


class QuerySetManager:
    model: Model


    @classmethod
    def get_queryset(cls, info, **kwargs) -> QuerySet:
        return cls.model.objects
    

    class Meta:
        abstract = True
        