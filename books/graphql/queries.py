import graphene
from graphene_django import DjangoListField

from books.graphql.types import BookType, AuthorType, ReviewType


class Query(graphene.ObjectType):
    books = DjangoListField(
        BookType
    )
    authors = DjangoListField(
        AuthorType,
    )
    reviews = DjangoListField(
        ReviewType
    )
