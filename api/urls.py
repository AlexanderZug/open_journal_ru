from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import InformationPageViewSet

router = SimpleRouter()

router.register('info', InformationPageViewSet, basename='info')

urlpatterns = [
    path('journal/', include(router.urls)),
]