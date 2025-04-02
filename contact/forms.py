from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
        }),
        label="Primeiro Nome",
        help_text="Informe o primeiro nome do contato",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'First Name',
        # })

    class Meta:
        model = models.Contact
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category',
                  )

        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'First Name',
        #     }
        #     ),
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                "O primeiro e o último nome devem ser diferentes",
                code='invalid',
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'abc':
            self.add_error(
                'first_name',
                ValidationError("Mensagem de erro")
            )

        return first_name
