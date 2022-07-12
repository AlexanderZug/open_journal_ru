from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse


class IndexPage(models.Model):
    title = models.CharField(verbose_name='название журнала',
                             max_length=250,
                             )
    head_img = models.ImageField(verbose_name='титульная фотография (опционально)',
                                 upload_to='head_img/%Y/%m/%d/',
                                 blank=True,
                                 null=True,
                                 )
    footer_color = ColorField(verbose_name='цвет футера (опционально)',
                              default='#FF0000',
                              blank=True,
                              )

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главная страница'

    def __str__(self):
        return self.title


class InformationPage(models.Model):
    reader = models.TextField(verbose_name='читателям', )
    authors = models.TextField(verbose_name='авторам', )
    library = models.TextField(verbose_name='библиотекам', )

    class Meta:
        verbose_name = 'страница с информацией'
        verbose_name_plural = 'страница с информацией'


class About(models.Model):
    journal = models.TextField(verbose_name='раздел о журнале', )
    editorial_team = models.TextField(verbose_name='раздел о редакции', )
    contact = models.CharField(verbose_name='контакты журнала',
                               max_length=300,
                               )

    class Meta:
        verbose_name = 'о журнале'
        verbose_name_plural = 'о журнале'


class Category(models.Model):
    category_name = models.CharField(verbose_name='категории',
                                     max_length=250, )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.category_name


class Archive(models.Model):
    issue_title = models.CharField(verbose_name='заголовок журнала (опционально)',
                                   max_length=250,
                                   blank=True,
                                   )
    issue_number = models.CharField(verbose_name='номер журнала',
                                    max_length=250,
                                    )
    issue_img = models.ImageField(verbose_name='фотография номера журнала (опционально)',
                                  upload_to='issue_img/%Y/%m/%d/',
                                  blank=True,
                                  null=True,
                                  )
    publish_date = models.DateField(verbose_name='дата публикации (автоматически)',
                                    auto_now_add=True,
                                    )
    all_issue_pdf = models.FileField(verbose_name='номер целиком (опционально)',
                                     upload_to='issue_pdf/',
                                     blank=True,
                                     )
    article_title = models.CharField(verbose_name='название статьи',
                                     max_length=300,
                                     )
    author = models.CharField(verbose_name='имя автора',
                              max_length=200,
                              )
    article_pdf = models.FileField(verbose_name='pdf-файл статьи',
                                   upload_to='issue_pdf/',
                                   )
    article = models.ForeignKey('Article',
                                verbose_name='статья',
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='articles',
                                )
    category = models.ForeignKey('Category',
                                 verbose_name='категория (опционально)',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='categories',
                                 )

    class Meta:
        ordering = ('-publish_date',)
        verbose_name = 'архив'
        verbose_name_plural = 'архив'

    def __str__(self):
        return self.issue_title


class Article(models.Model):
    affiliation = models.CharField(verbose_name='аффилиация',
                                   max_length=350,
                                   )
    keywords = models.CharField(verbose_name='ключевые слова',
                                max_length=300,
                                )
    summary = models.TextField(verbose_name='аннотация', )
    archive = models.ForeignKey('Archive',
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='articles',
                                )

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.affiliation

    # def get_absolute_url(self):
    #     return reverse('article_detail', kwargs={'id': self.id})
