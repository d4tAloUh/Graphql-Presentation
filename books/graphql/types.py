from graphene_django import DjangoObjectType

from books.graphql.utils import login_required
from books.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'description',
                  'authors', 'created_at', 'updated_at')

    #
    # @classmethod
    # @login_required
    # def get_queryset(cls, queryset, info):
    #     return queryset.filter(user=info.context.user)
