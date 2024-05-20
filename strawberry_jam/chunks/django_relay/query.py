# TODO

type_class = """
@strawberry.type(name="Query")
class {query_name_pascal_case}:
"""

field = """
    {query_field_name_pascal_case}: strawberry_django.relay.ListConnectionWithTotalCount[{node_name_pascal_case}] = strawberry_django.connection()
"""
