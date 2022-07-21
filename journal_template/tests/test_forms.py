from django.test import TestCase, Client

from journal_template.forms import ClientContactForm


class FormTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.form = ClientContactForm()

    def test_forms_widget(self):
        """Тестирование placeholder из класса Meta."""
        placeholder = self.form.fields['massage'].widget.attrs[
            'placeholder']
        self.assertEqual(placeholder, 'Введите сообщение')

    def test_forms_help_text(self):
        """Тестирование help_text из класса Meta."""
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
