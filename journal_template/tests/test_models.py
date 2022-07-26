from django.test import TestCase

from journal_template.models import (
    About,
    Archive,
    Article,
    Category,
    ClientContact,
    IndexPage,
    InformationPage,
)


class ModelTests(TestCase):
    def setUp(self):
        self.index_model = IndexPage.objects.create()
        self.info_page = InformationPage.objects.create()
        self.about = About.objects.create()
        self.client_contact = ClientContact.objects.create()
        self.archive = Archive.objects.create()
        self.article = Article.objects.create(pk=2)
        self.category = Category.objects.create()

    def test_index_page_verbose_name(self):
        """Check verbose_names in IndexPage model."""
        fields_verbose = {
            'title': 'название журнала',
            'head_img': 'титульная фотография (опционально)',
            'footer_color': 'цвет футера (опционально)',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(
                    self.index_model._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_info_page_verbose_name(self):
        """Check verbose_names in InformationPage model."""
        fields_verbose = {
            'reader': 'читателям',
            'authors': 'авторам',
            'library': 'библиотекам',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(
                    self.info_page._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_about_page_verbose_name(self):
        """Check verbose_names in About model."""
        fields_verbose = {
            'journal': 'раздел о журнале',
            'editorial_team': 'раздел о редакции',
            'contact': 'контакты журнала',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(
                    self.about._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_client_contact_verbose_name(self):
        """Check verbose_names in ClientContact model."""
        fields_verbose = {
            'name': 'имя',
            'surname': 'фамилия',
            'email': 'email',
            'massage': 'текст сообщения',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(
                    self.client_contact._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_archive_verbose_name(self):
        """Check verbose_names in Archive model."""
        fields_verbose = {
            'issue_title': 'заголовок журнала (опционально)',
            'issue_number': 'номер журнала',
            'issue_img': 'фотография номера журнала (опционально)',
            'all_issue_pdf': 'номер целиком (опционально)',
            'article': 'статья|автор статьи (необходимо заполнить)',
        }
        for field, expected_value in fields_verbose.items():
            with self.subTest(field=field):
                self.assertEquals(
                    self.archive._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_article_verbose_name(self):
        """Check verbose_names in Article model."""
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
                self.assertEquals(
                    self.article._meta.get_field(field).verbose_name,
                    expected_value,
                )

    def test_category_verbose_name(self):
        """Check verbose_name in Category model."""
        verbose = self.category._meta.get_field('category_name').verbose_name
        self.assertEquals(verbose, 'категории')

    def test__str__(self):
        """Check __str__ in all models."""
        fields_str = {
            f'{self.index_model}': f'{self.index_model.title}',
            f'{self.info_page}': f'{self.info_page.reader}',
            f'{self.about}': f'{self.about.journal}',
            f'{self.client_contact}': f'{self.client_contact.surname}',
            f'{self.archive}': f'{self.archive.issue_title}',
            f'{self.article}': f'{"%s | %s" % (self.article.author, self.article.article_title)}',
        }
        for field, expected_object_name in fields_str.items():
            with self.subTest(field=field):
                self.assertEquals(expected_object_name, str(field))

    def test_get_absolute_url_article(self):
        """Check get_absolute_url in Article model."""
        self.assertEquals(
            self.article.get_absolute_url(), '/article_detail/2/'
        )
