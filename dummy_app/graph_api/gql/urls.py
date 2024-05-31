
from django.urls import path
from strawberry.django.views import GraphQLView

from graph_api.gql.schema import schema

urlpatterns = [
    path('', GraphQLView.as_view(schema=schema)),
]
