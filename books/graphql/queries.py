import graphene
from graphene_django import DjangoListField

from books.graphql.types import BookType, AuthorType, ReviewType
from books.models import Book


class Query(graphene.ObjectType):
    books = DjangoListField(
        BookType
    )
    book_exact = DjangoListField(
        BookType,
        isbn=graphene.ID(required=True)
    )

    authors = DjangoListField(
        AuthorType,
    )
    reviews = DjangoListField(
        ReviewType
    )

    def resolve_book_exact(self, info, isbn):
        return Book.objects.filter(isbn=isbn)
