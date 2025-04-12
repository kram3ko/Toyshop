from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from customers.forms import (
    CustomerUpdateForm,
    ToyClubCreationForm,
)
from customers.models import ToyClub, User


class CustomersListView(generic.ListView):
    model = User
    template_name = "toyshop/customers/customer_list.html"
    paginate_by = 10


class CustomerProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "toyshop/customers/profile.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            return render(self.request, "toyshop/customers/customer_form.html", context)
        return super().render_to_response(context, **response_kwargs)


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
    fields = [
        "user",
    ]
    template_name = "toyshop/customers/toy_club_assign.html"
    success_url = reverse_lazy("customers:toy-club-list")
