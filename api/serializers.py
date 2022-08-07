from rest_framework import serializers

from journal_template.models import Archive, Article, ClientContact


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = ('name', 'surname', 'email', 'massage',)


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'article_title',
            'author',
            'article_pdf',
            'affiliation',
            'keywords',
            'summary',
            'category',
        )


class ArchiveSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Archive
        fields = (
            'id',
            'issue_title',
            'issue_number',
            'issue_img',
            'all_issue_pdf',
            'article',
        )
