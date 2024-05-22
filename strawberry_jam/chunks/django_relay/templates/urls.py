

output = """
from django.urls import path
from strawberry.django.views import GraphQLView

from {schema_app_label}.{api_folder_name}.schema import schema

urlpatterns = [
    path('graphql', GraphQLView.as_view(schema=schema)),
]
"""