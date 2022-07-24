from http import HTTPStatus
from typing import NamedTuple

from django import forms
from django.test import Client, TestCase
from django.urls import reverse

from journal_template.models import Article, Archive


class NameAndTemplate(NamedTuple):
    """Schema for names and templates."""

    name: str
    template: str


class ViewTest(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.article_model = Article.objects.create()
        self.archive_model = Archive.objects.create()
        self.name_template = {
            'index': NameAndTemplate(
                name=reverse('journal_template:index'),
                template='index.html'
            ),
            'info': NameAndTemplate(
                name=reverse('journal_template:info'),
                template='info.html'
            ),
            'about': NameAndTemplate(
                name=reverse('journal_template:about'),
                template='about.html'
            ),
            'archive': NameAndTemplate(
                name=reverse('journal_template:archive'),
                template='archive.html'
            ),
            'article_detail': NameAndTemplate(
                name=reverse('journal_template:article_detail',
                             kwargs={'slug': self.article_model.pk}),
                template='article_detail.html'
            ),
            'archive_detail': NameAndTemplate(
                name=reverse('journal_template:archive_detail',
                             kwargs={'slug': self.archive_model.pk}),
                template='archive_detail.html'
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
                self.assertTemplateUsed(response, names_and_template.template)

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
