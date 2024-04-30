from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "style": "background:rgba(35,146,157,0.3);",
            }
        ),
        validators=[
            validators.RegexValidator(
                r"^[\w.+\-]+$",
                (
                    "Enter a valid username. This value may contain only "
                    "letters, numbers, spaces "
                    "and ./+/-/_ characters."
                ),
            ),
        ],
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "style": "background:rgba(35,146,157,0.3);",
            }
        ),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "style": "background:rgba(35,146,157,0.3);",
            }
        ),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "style": "background:rgba(35,146,157,0.3);",
            }
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "style": "background:rgba(35,146,157,0.3);"}
        ),
        validators=[validate_password],
    )

    password2 = forms.CharField(
        label="Re-Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "style": "background:rgba(35,146,157,0.3);"}
        ),
    )

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
                raise forms.ValidationError("Passwords do not match.")
            return self.cleaned_data["password2"]
        else:
            raise forms.ValidationError("Passwords do not match!")

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("A user with that email already exists.")

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data["username"]).exists():
            raise forms.ValidationError("A user with that username already exists.")
