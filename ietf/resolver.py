# Copyright Amazon Q & AHMED OUARDI 2024, All Rights Reserved
# GraphQL Resolver Configuration for IETF Datatracker

import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from ietf.doc.models import Document
from ietf.person.models import Person
from ietf.group.models import Group


class UserType(DjangoObjectType):
    """GraphQL type for User model"""
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "is_active")


class DocumentType(DjangoObjectType):
    """GraphQL type for Document model"""
    class Meta:
        model = Document
        fields = ("name", "title", "abstract", "rev", "type", "stream", "group", "states")


class PersonType(DjangoObjectType):
    """GraphQL type for Person model"""
    class Meta:
        model = Person
        fields = ("id", "name", "ascii", "email", "user")


class GroupType(DjangoObjectType):
    """GraphQL type for Group model"""
    class Meta:
        model = Group
        fields = ("id", "name", "acronym", "type", "state", "description")


class Query(graphene.ObjectType):
    """Main GraphQL Query resolver"""
    
    # User queries
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    
    # Document queries
    all_documents = graphene.List(DocumentType)
    document_by_name = graphene.Field(DocumentType, name=graphene.String(required=True))
    
    # Person queries
    all_persons = graphene.List(PersonType)
    person_by_id = graphene.Field(PersonType, id=graphene.Int(required=True))
    
    # Group queries
    all_groups = graphene.List(GroupType)
    group_by_acronym = graphene.Field(GroupType, acronym=graphene.String(required=True))

    def resolve_all_users(self, info):
        """Resolve all users query"""
        return User.objects.filter(is_active=True)

    def resolve_user_by_id(self, info, id):
        """Resolve user by ID query"""
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def resolve_all_documents(self, info):
        """Resolve all documents query"""
        return Document.objects.all()[:100]  # Limit for performance

    def resolve_document_by_name(self, info, name):
        """Resolve document by name query"""
        try:
            return Document.objects.get(name=name)
        except Document.DoesNotExist:
            return None

    def resolve_all_persons(self, info):
        """Resolve all persons query"""
        return Person.objects.all()[:100]  # Limit for performance

    def resolve_person_by_id(self, info, id):
        """Resolve person by ID query"""
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            return None

    def resolve_all_groups(self, info):
        """Resolve all groups query"""
        return Group.objects.all()

    def resolve_group_by_acronym(self, info, acronym):
        """Resolve group by acronym query"""
        try:
            return Group.objects.get(acronym=acronym)
        except Group.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    """GraphQL Mutations (placeholder for future use)"""
    pass


# Main GraphQL schema
schema = graphene.Schema(query=Query, mutation=Mutation)