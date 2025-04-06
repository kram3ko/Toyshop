from django import forms
from wishlists.models import WishList

class WishListCreateForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ["title"]
