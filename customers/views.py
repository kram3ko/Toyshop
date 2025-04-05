from django.views import generic

from customers.models import User
from toys.models import Category


class CustomersListView(generic.ListView):
    model = User
    template_name = "toyshop/customers/customer_list.html"

class CustomerDetailView(generic.DetailView):
    model = User
    template_name = "toyshop/customers/customer_detail.html"