from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from books.graphql.utils import login_required
from books.models import Book, Review, Author

User = get_user_model()


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'description',
                  'authors', 'created_at', 'updated_at',
                  'reviews')

    #
    # @classmethod
    # @login_required
    # def get_queryset(cls, queryset, info):
    #     return queryset.filter(user=info.context.user)


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name')


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ('id', 'rating', 'user', 'book',
                  'description')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'is_staff')
