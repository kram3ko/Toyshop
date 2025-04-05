from django import forms
from django.contrib.auth.forms import UserCreationForm

from customers.models import User
from customers.validators import ExactLenValidator, FirstUpperLetter, LastDigits


class LicenseNumberFieldMixin:
    LEN_LICENSE = 8
    FIRST_UPPER = 3
    LAST_DIGITS = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["license_number"] = forms.CharField(
            required=True,
            help_text=f"""Your license must contain"
                      at least {self.LEN_LICENSE} characters.
                      First {self.FIRST_UPPER} must be uppercase letters.
                      Last {self.LAST_DIGITS} must be digits.""",
            validators=[
                ExactLenValidator(limit_value=self.LEN_LICENSE),
                FirstUpperLetter(limit_value=self.FIRST_UPPER),
                LastDigits(limit_value=self.LAST_DIGITS)
            ]
        )


class CustomCustomerCreationForm(LicenseNumberFieldMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "",
        )


class CustomerLicenseUpdateForm(LicenseNumberFieldMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("license_number",)



class SingleFieldSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search...",
                "class": "form-control w-50"
            }
        )
    )
