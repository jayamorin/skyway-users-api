import graphene
import users.schema

class Query(users.schema.Query):
    pass


class Mutation(users.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
