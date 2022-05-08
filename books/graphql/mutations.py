import graphene
from django.db.transaction import atomic
from graphene_django.forms.mutation import DjangoModelFormMutation

from books.forms import AuthorForm, ReviewForm, BookForm
from books.graphql.types import AuthorType, ReviewType, BookType
from books.models import Book, Review, Author


class CreateAuthorMutation(DjangoModelFormMutation):
    author = graphene.Field(AuthorType)

    class Meta:
        form_class = AuthorForm

    @classmethod
    def perform_mutate(cls, form, info):
        return super().perform_mutate(form, info)


class CreateReviewMutation(DjangoModelFormMutation):
    review = graphene.Field(ReviewType)

    class Meta:
        form_class = ReviewForm

    @classmethod
    def perform_mutate(cls, form, info):
        return super().perform_mutate(form, info)


class CreateBookMutation(DjangoModelFormMutation):
    book = graphene.Field(BookType)

    class Meta:
        form_class = BookForm

    @classmethod
    @atomic
    def perform_mutate(cls, form, info):
        authors = form.cleaned_data.pop('authors', [])
        book = form.save()
        book.authors.set(authors)
        return super().perform_mutate(form, info)


class Mutation(
    graphene.ObjectType
):
    create_author = CreateAuthorMutation.Field()
    create_review = CreateReviewMutation.Field()
    create_book = CreateBookMutation.Field()
