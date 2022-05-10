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

    # def default_resolver(attname, default_value, root, info, **args):
    #     """
    #     Staff with permissions can see all attributes.
    #     Everyone else can only see id and title.
    #     """
    #     user = info.context.user
    #     # Return all fields if user is admin
    #     if user.is_active and user.is_staff and \
    #             user.has_perm(''):
    #         return dict_or_attr_resolver(attname, default_value, root,
    #                                      info, **args)
    #     customer_fields = (
    #         'id', 'title'
    #     )
    #     try:
    #         user.customerprofile
    #     except CustomerProfile.DoesNotExist:
    #         raise PermissionDenied('You do not have permissions to '
    #                                'access this resource')
    #     else:
    #         if attname in customer_fields:
    #             return dict_or_attr_resolver(attname, default_value, root,
    #                                          info, **args)
    #
    #     raise PermissionDenied('You do not have permissions to '
    #                            'access this resource')


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', "surname", "birth_date")

    def resolve_surname(self, info):
        return self.surname


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ('id', 'rating', 'user', 'book',
                  'description')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'
