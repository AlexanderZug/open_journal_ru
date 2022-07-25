import random
import string
from http import HTTPStatus
from typing import NamedTuple

from django.test import Client, TestCase

from journal_template.models import Article, Archive


class UrlAndTemplate(NamedTuple):
    """Schema for urls and templates."""

    url: str
    template: str


class URLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.article_model = Article.objects.create()
        self.archive_model = Archive.objects.create()
        self.urls = {
            'index': UrlAndTemplate(
                url='/',
                template='index.html'
            ),
            'info_page': UrlAndTemplate(
                url='/info_page/',
                template='info.html'
            ),
            'about': UrlAndTemplate(
                url='/about/',
                template='about.html'
            ),
            'archive': UrlAndTemplate(
                url='/archive/',
                template='archive.html'
            ),
            'article_detail': UrlAndTemplate(
                url=f'/article_detail/{self.article_model.pk}/',
                template='article_detail.html'
            ),
            'archive_detail': UrlAndTemplate(
                url=f'/archive_detail/{self.archive_model.pk}/',
                template='archive_detail.html'
            )
        }
        self.errors = {
            'error_404': UrlAndTemplate(
                url='/some_url/',
                template='errors/404.html',
            )
        }

    def test_urls_exist_at_desired_location(self):
        """Check urls accuses to guest user."""
        for url in self.urls.values():
            with self.subTest(url=url.url):
                status_code = self.guest_client.get(url.url).status_code
                self.assertEqual(status_code, HTTPStatus.OK)

    def test_correct_template(self):
        """Check correct templates."""
        for page in self.urls.values():
            with self.subTest(page=page.url):
                response = self.guest_client.get(page.url)
                self.assertTemplateUsed(response, page.template)

    def test_unexciting_page(self):
        """Unexciting page returns html 404."""
        letters = string.ascii_lowercase
        response = self.guest_client.get(
            f'/{"/".join(random.choice(letters) for _ in range(10))}/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertTemplateUsed(response, self.errors['error_404'].template)
