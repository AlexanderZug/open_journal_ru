from rest_framework import serializers

from journal_template.models import InformationPage


class InformationPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationPage
        fields = '__all__'
