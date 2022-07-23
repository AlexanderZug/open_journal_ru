from django.test import TestCase

from journal_template.models import (About, Archive, Article, Category,
                                     ClientContact, IndexPage, InformationPage)


class ModelTests(TestCase):
    def setUp(self):
        self.index_model = IndexPage.objects.create()
        self.info_page = InformationPage.objects.create()
        self.about = About.objects.create()
        self.client_contact = ClientContact.objects.create()
        self.archive = Archive.objects.create()
        self.article = Article.objects.create()
        self.category = Category.objects.create()

    def test_index_page_verbose_name(self):
        fields_verbose = {
            'title': 'название журнала',
            'head_img': 'титульная фотография (опционально)',
            'footer_color': 'цвет футера (опционально)',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.index_model._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_info_page_verbose_name(self):
        fields_verbose = {
            'reader': 'читателям',
            'authors': 'авторам',
            'library': 'библиотекам',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.info_page._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_about_page_verbose_name(self):
        fields_verbose = {
            'journal': 'раздел о журнале',
            'editorial_team': 'раздел о редакции',
            'contact': 'контакты журнала',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.about._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_client_contact_verbose_name(self):
        fields_verbose = {
            'name': 'имя',
            'surname': 'фамилия',
            'email': 'email',
            'massage': 'текст сообщения',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.client_contact._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_archive_verbose_name(self):
        fields_verbose = {
            'issue_title': 'заголовок журнала (опционально)',
            'issue_number': 'номер журнала',
            'issue_img': 'фотография номера журнала (опционально)',
            'all_issue_pdf': 'номер целиком (опционально)',
            'article': 'статья|автор статьи (необходимо заполнить)',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.archive._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_article_verbose_name(self):
        fields_verbose = {
            'article_title': 'название статьи',
            'author': 'имя автора',
            'article_pdf': 'pdf-файл статьи',
            'affiliation': 'аффилиация',
            'keywords': 'ключевые слова',
            'summary': 'аннотация',
            'category': 'категория (опционально)',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(self.article._meta.get_field(field).verbose_name,
                                  expected_value)

    def test_category_verbose_name(self):
        verbose = self.category._meta.get_field('category_name').verbose_name
        self.assertEquals(verbose, 'категории')
