import graphene
from graphene_django import DjangoObjectType

from users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)
