from rest_framework.routers import DefaultRouter

from books.rest.views import BookViewSet, ReviewViewSet, AuthorViewSet, BookReviewsViewSet

router = DefaultRouter()

router.register(
    r'books',
    BookViewSet,
    basename='book'
)
router.register(
    r'authors',
    AuthorViewSet,
    basename='author'
)

router.register(
    r'reviews',
    ReviewViewSet,
    basename='review'
)

router.register(
    r'reviews/book/(?P<book_id>[0-9]+)',
    BookReviewsViewSet,
    basename='book-review'
)

urlpatterns = router.urls
