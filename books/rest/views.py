from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from books.models import Book, Author, Review
from books.rest.serializers import BookSerializer, AuthorSerializer, ReviewSerializer


class BookViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
