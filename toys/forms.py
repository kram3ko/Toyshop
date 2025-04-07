from django import forms

from toys.models import Toy, Category


class ToyCreateForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Toy
        fields = [
            "name",
            "description",
            "price",
            "stock",
            "manufacturer",
            "category",
            "photo"
        ]

class ToySearchForm(forms.Form):
    toy = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search toy",
                "class": "form-control w-50"
            }
        )
    )
