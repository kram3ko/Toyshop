from django.views import generic

from customers.models import User
from toys.models import Category


class CustomersListView(generic.ListView):
    model = User
    template_name = "toyshop/customers/customer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context