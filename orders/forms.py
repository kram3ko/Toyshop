from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "payment_method",
            "delivery_method",
            "deliver_to",
            "recipient"
        ]
