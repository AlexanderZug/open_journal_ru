from django import forms

from .models import ClientContact


class ClientContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['massage'].widget.attrs['placeholder'] = (
            'Введите сообщение'
        )

    class Meta:
        model = ClientContact
        fields = '__all__'
        help_texts = {
            'name': 'Введите имя.',
            'surname': 'Введите фамилию.',
            'email': 'Введите почту.',
        }
