from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from customers.models import ToyClub
from customers.validators import ExactLenValidator, FirstUpperLetter, LastDigits

User = get_user_model()


class CustomCustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email address")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class CustomerUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False, label="Email address")
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class ToyClubCreationForm(forms.ModelForm):
    LEN_NUMBER = 10
    FIRST_UPPER = 3
    LAST_DIGITS = 7

    unique_number = forms.CharField(
        required=True,
        help_text=f"""Your license must contain"
                      at least {LEN_NUMBER} characters.
                      First {FIRST_UPPER} must be uppercase letters.
                      Last {LAST_DIGITS} must be digits.""",
        validators=[
            ExactLenValidator(limit_value=LEN_NUMBER),
            FirstUpperLetter(limit_value=FIRST_UPPER),
            LastDigits(limit_value=LAST_DIGITS),
        ],
    )

    class Meta:
        model = ToyClub
        fields = (
            "user",
            "level",
            "unique_number",
        )
