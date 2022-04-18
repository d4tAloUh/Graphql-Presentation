import graphene
from graphene_django import DjangoListField

from books.graphql.types import BookType


class BooksQuery(graphene.ObjectType):
    books = DjangoListField(
        BookType,
    )


class Query(BooksQuery):
    pass
