import graphene

from books.graphql import (
    queries as books_queries,
    mutations as books_mutations,
)


class Query(books_queries.Query, graphene.ObjectType):
    pass


# class Mutation(books_mutations.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query
                         # mutation=Mutation
                         )
