from django.test import Client, TestCase
from django.urls import reverse

from journal_template.forms import ClientContactForm
from journal_template.models import ClientContact


class FormTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.contact_count = ClientContact.objects.count()
        self.form = ClientContactForm()

    def test_create_contact(self):
        """Check redirect and amount on records correct data to the DB."""
        response = self.guest_client.post(
            reverse('journal_template:info'),
            data={'name': 'test name',
                  'surname': 'test surname',
                  'email': 'test_test@test.com',
                  'massage': 'some text',
                  }
        )
        self.assertRedirects(response, reverse('journal_template:index'))
        self.assertEqual(ClientContact.objects.count(), self.contact_count + 1)
        self.assertTrue(ClientContact.objects.filter(name='test name',
                                                     surname='test surname',
                                                     email='test_test@test.com',
                                                     massage='some text').exists())

    def test_forms_widget(self):
        """Check placeholder from class Meta, form ClientContactForm."""
        placeholder = self.form.fields['massage'].widget.attrs[
            'placeholder']
        self.assertEqual(placeholder, 'Введите сообщение')

    def test_forms_help_text(self):
        """Check help_text from class Meta, form ClientContactForm."""
        help_text_forms = self.form
        field_help_text = {
            'name': 'Введите имя.',
            'surname': 'Введите фамилию.',
            'email': 'Введите почту.',
        }
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    help_text_forms[field].help_text, expected_value)
