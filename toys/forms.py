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
                "class": (
                    "w-full h-11 px-4 py-2 rounded-l-md border border-gray-300 "
                    "text-black focus:outline-none focus:ring-2 focus:ring-blue-500"
                )
            }
        )
    )

