from django.contrib import admin

from .models import (About, Archive, Article, Category, IndexPage,
                     InformationPage)


class IndexPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'head_img',
        'footer_color',
    )


class InformationPageAdmin(admin.ModelAdmin):
    list_display = (
        'reader',
        'authors',
        'library',
    )


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'journal',
        'editorial_team',
        'contact',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )


class ArchiveAdmin(admin.ModelAdmin):
    list_display = (
        'issue_title',
        'issue_number',
        'issue_img',
        'publish_date',
        'all_issue_pdf',
        'article',

    )
    search_fields = ('author',)
    list_filter = ('publish_date',)
    empty_value_display = '-пусто-'


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'affiliation',
        'keywords',
        'summary',
        'archive',
        'article_title',
        'author',
        'article_pdf',
        'category',
    )
    search_fields = ('author',)


admin.site.register(IndexPage, IndexPageAdmin)
admin.site.register(InformationPage, InformationPageAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Article, ArticleAdmin)
