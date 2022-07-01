from django.db import models
from colorfield.fields import ColorField


class IndexPage(models.Model):
    title = models.CharField(max_length=250)
    head_img = models.ImageField(upload_to='head_img/%Y/%m/%d/',
                                 blank=True,
                                 null=True,
                                 )
    footer_color = ColorField(default='#FF0000')


class InformationPage(models.Model):
    reader = models.TextField()
    authors = models.TextField()
    library = models.TextField()


class About(models.Model):
    journal = models.TextField()
    editorial_team = models.TextField()
    contact = models.CharField(max_length=300)


class Category(models.Model):
    category_name = models.CharField(max_length=250)


class Archive(models.Model):
    issue_title = models.CharField(max_length=250)
    issue_img = models.ImageField(upload_to='issue_img/%Y/%m/%d/',
                                  blank=True,
                                  null=True,
                                  )
    publish_date = models.DateField(auto_now_add=True)
    all_issue_pdf = models.FileField(upload_to='issue_pdf/')
    article_title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    article_pdf = models.FileField(upload_to='issue_pdf/')
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='categories')


class Article(models.Model):
    affiliation = models.CharField(max_length=350)
    keywords = models.CharField(max_length=300)
    summary = models.TextField()
    archive = models.ForeignKey('Archive',
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='articles')
