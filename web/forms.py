from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя',
                   'id': '"name_input_form',
                   'class': 'input-at'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш E-mail',
                   'id': '"email_input_form',
                   'class': 'input-at'}
        )
    )

    message = forms.CharField(
        min_length=5,
        widget=forms.Textarea(
            attrs={'placeholder': 'Ваше сообщение',
                   'id': '"text_input_form',
                   'class': 'input-at'}
        )
    )

    file = forms.FileField(
        label="Загрузить файл",
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'content_add_file'}
        )
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'хуйло':
            raise ValidationError('Заявки от ХУЙЛУШИ не рассматриваем!!')

        return name