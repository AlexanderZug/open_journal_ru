from http import HTTPStatus
from typing import NamedTuple

from django import forms
from django.test import Client, TestCase
from django.urls import reverse

from journal_template.models import Archive, Article
from open_journal_ru.settings import ARCHIVES_PER_PAGE


class PageContentSchema(NamedTuple):
    """Schema for names, templates and second page URL."""

    name: str
    value: str


class ViewTest(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.article_model = Article.objects.create()
        self.archive_model = Archive.objects.create()
        self.name_template = {
            'index': PageContentSchema(
                name=reverse('journal_template:index'),
                value='index.html'
            ),
            'info': PageContentSchema(
                name=reverse('journal_template:info'),
                value='info.html'
            ),
            'about': PageContentSchema(
                name=reverse('journal_template:about'),
                value='about.html'
            ),
            'archive': PageContentSchema(
                name=reverse('journal_template:archive'),
                value='archive.html'
            ),
            'article_detail': PageContentSchema(
                name=reverse('journal_template:article_detail',
                             kwargs={'slug': self.article_model.pk}),
                value='article_detail.html'
            ),
            'archive_detail': PageContentSchema(
                name=reverse('journal_template:archive_detail',
                             kwargs={'slug': self.archive_model.pk}),
                value='archive_detail.html'
            )
        }
        self.form_fields = {
            'name': forms.fields.CharField,
            'surname': forms.fields.CharField,
            'email': forms.fields.EmailField,
            'massage': forms.fields.CharField,
        }

    def test_view_use_correct_template(self):
        """Check URL uses correct template."""
        for names_and_template in self.name_template.values():
            with self.subTest(template=names_and_template.name):
                response = self.guest_client.get(names_and_template.name)
                self.assertTemplateUsed(response, names_and_template.value)

    def test_view_url_accessible_by_name(self):
        """Check URL is accessible by name."""
        for reversed_name in self.name_template.values():
            with self.subTest(reversed_name=reversed_name):
                response = self.guest_client.get(reversed_name.name)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_create_show_correct_instance(self):
        """Check form's fields."""
        for field, expected in self.form_fields.items():
            with self.subTest(field=field):
                response = self.guest_client.get(
                    self.name_template['info'].name)
                form_field = response.context.get('form').fields.get(field)
                self.assertIsInstance(form_field, expected)


class PaginatorTest(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.archive_model = [Archive.objects.create(issue_number=f'Issues {i}')
                              for i in range(ARCHIVES_PER_PAGE * 2)]
        self.paginator = {'archive': PageContentSchema(
            name=reverse('journal_template:archive'),
            value='?page=2'
        )}

    def test_paginator_first_page(self):
        """Check that paginator gives 5 archives per page."""
        response = self.guest_client.get(self.paginator['archive'].name)
        self.assertEqual(len(response.context.get('page_obj').object_list),
                         ARCHIVES_PER_PAGE)

    def test_paginator_next_page(self):
        """Check that paginator shows archives on the second page."""
        posts_number_on_next_page = (ARCHIVES_PER_PAGE * 2
                                     - ARCHIVES_PER_PAGE)
        response = self.guest_client.get(self.paginator['archive'].name
                                         + self.paginator['archive'].value)
        self.assertEqual(len(response.context.get('page_obj').object_list),
                         posts_number_on_next_page)
