from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from customers.forms import CustomCustomerCreationForm
from customers.models import User


class CustomersListView(generic.ListView):
    model = User
    template_name = "toyshop/customers/customer_list.html"

class CustomerProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "toyshop/customers/profile.html"


class CustomerRegisterView(generic.CreateView):
    model = User
    template_name = "toyshop/customers/register.html"
    form_class = CustomCustomerCreationForm
    success_url = reverse_lazy("login")