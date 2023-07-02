import graphene
import graphene_django

from .models import User

class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    def mutate(self, info, first_name, last_name, email):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.UUID()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    def mutate(self, info, id, first_name, last_name, email):
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return UpdateUser(ok=True, user=user)


class DeleteUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.UUID()

    def mutate(self, info, id):
        user = User.objects.get(id=id)
        user.delete()
        return DeleteUser(ok=True)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
