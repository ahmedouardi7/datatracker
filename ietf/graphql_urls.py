# Copyright Amazon Q & AHMED OUARDI 2024, All Rights Reserved
# GraphQL URL Configuration for IETF Datatracker

from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .resolver import schema

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('graphql/api/', csrf_exempt(GraphQLView.as_view(schema=schema))),
]