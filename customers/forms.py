from django import forms
from django.contrib.auth.forms import UserCreationForm

from customers.models import User, ToyClub
from customers.validators import (
    ExactLenValidator,
    FirstUpperLetter,
    LastDigits
)


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


class CustomCustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class ToyClubUniqueNumberUpdateForm(LicenseNumberFieldMixin, forms.ModelForm):
    class Meta:
        model = ToyClub
        fields = ("unique_number",)
