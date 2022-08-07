from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import ArchiveViewSet, ArticleViewSet, ClientContactViewSet

router = SimpleRouter()

router.register('contact', ClientContactViewSet, basename='contact')
router.register('article', ArticleViewSet, basename='article')
router.register('archive', ArchiveViewSet, basename='archive')

urlpatterns = [
    path('journal/', include(router.urls)),
]
