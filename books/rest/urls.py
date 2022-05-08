from rest_framework.routers import DefaultRouter

from books.rest.views import BookViewSet, ReviewViewSet, AuthorViewSet

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

urlpatterns = router.urls
