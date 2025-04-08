from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from customers.forms import CustomCustomerCreationForm, CustomerUpdateForm, ToyClubCreationForm
from customers.models import User, ToyClub


class CustomersListView(generic.ListView):
    model = User
    template_name = "toyshop/customers/customer_list.html"
    paginate_by = 10

class CustomerProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "toyshop/customers/profile.html"


class CustomerRegisterView(generic.CreateView):
    model = User
    template_name = "toyshop/customers/register.html"
    form_class = CustomCustomerCreationForm
    success_url = reverse_lazy("login")


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = CustomerUpdateForm
    template_name = "toyshop/customers/customer_form.html"


class ToyClubCreateView(LoginRequiredMixin, generic.CreateView):
    model = ToyClub
    form_class = ToyClubCreationForm
    template_name = "toyshop/customers/toy_club_form.html"
    success_url = reverse_lazy("customers:toy-club-list")

class ToyClubListView(LoginRequiredMixin, generic.ListView):
    model = ToyClub
    template_name = "toyshop/customers/toy_club_list.html"

class ToyClubAssignView(LoginRequiredMixin, generic.UpdateView):
    model = ToyClub
    fields = ["user",]
    template_name = "toyshop/customers/toy_club_assign.html"
    success_url = reverse_lazy("customers:toy-club-list")