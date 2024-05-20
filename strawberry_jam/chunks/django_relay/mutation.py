# TODO

type_class = """
@strawberry.type(name="Mutation")
class {mutation_name_pascal_case}:

    @strawberry_django.mutation(handle_django_errors=True)
    def create_{mutation_field_name}(self, data: dict):
        form = {create_form_name_pascal_case}(data)
        return cast({node_name_pascal_case}, form.save())

    @strawberry_django.mutation(handle_django_errors=True)
    def create_{mutation_field_name}(self, data: dict):
        form = {update_form_name_pascal_case}(data)
        return cast({node_name_pascal_case}, form.save())

    delete_{mutation_field_name}: {node_name_pascal_case} = strawberry_django.mutations.{operation_name}(
        strawberry_django.NodeInput,
        handle_django_errors=True
    )

"""
