from django.contrib import admin
from .models import IndexPage, InformationPage, About, Archive, Article, Category


class IndexPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'head_img',
        'footer_color',
    )


class ArchiveAdmin(admin.ModelAdmin):
    list_display = (
        'issue_title',
        'issue_img',
        'publish_date',
        'all_issue_pdf',
        'article_title',
        'author',
        'article_pdf',
        'category',
    )
    search_fields = ('author',)
    list_filter = ('publish_date',)
    empty_value_display = '-пусто-'


admin.site.register(IndexPage, IndexPageAdmin)
admin.site.register(InformationPage)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Article)
