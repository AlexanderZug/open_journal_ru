from rest_framework.viewsets import ModelViewSet

from api.serializers import (
    ArchiveSerializer,
    ArticleSerializer,
    ClientContactSerializer,
)
from journal_template.models import Archive, Article, ClientContact


class ClientContactViewSet(ModelViewSet):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArchiveViewSet(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
