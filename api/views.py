from rest_framework.viewsets import ModelViewSet

from api.serializers import InformationPageSerializer


from journal_template.models import InformationPage


class InformationPageViewSet(ModelViewSet):
    queryset = InformationPage.objects.all()
    serializer_class = InformationPageSerializer
