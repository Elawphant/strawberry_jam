

from strawberry.relay import Node
from strawberry_jam.queryset import QuerySetManager


class Node(Node):

    @classmethod
    def get_queryset(cls, queryset, info, **kwargs):
        return cls.queryset_manager.get_queryset(info, **kwargs)

    class Meta:
        queryset_manager: QuerySetManager
        abstract = True

