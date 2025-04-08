from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            'accept': 'image/*',

        }),
    )

    class Meta:
        model = models.Contact
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category',
                  'picture',
                  )

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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, max_length=30, required=True)
    last_name = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError(
                "Email já cadastrado", code='invalid'))

        return email
