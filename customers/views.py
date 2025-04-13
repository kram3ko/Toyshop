from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from customers.forms import (
    CustomerUpdateForm,
    ToyClubCreationForm,
)
from customers.models import ToyClub

User = get_user_model()


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    success_url = reverse_lazy("customers:customers-list")
class CustomersListView(LoginRequiredMixin, generic.ListView):
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


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "toyshop/customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customers:customers-list")


class ToyClubCreateView(LoginRequiredMixin, generic.CreateView):
    model = ToyClub
    form_class = ToyClubCreationForm
    template_name = "toyshop/customers/toy_club_form.html"
    success_url = reverse_lazy("customers:toy-club-list")


class ToyClubListView(LoginRequiredMixin, generic.ListView):
    model = ToyClub
    template_name = "toyshop/customers/toy_club_list.html"

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["club_to_user"] = self.request.POST.get("club_to_user")
        return context

    def get_queryset(self):
        queryset = ToyClub.objects.all()
        user_id = self.request.POST.get("club_to_user")
        if user_id:
            queryset = queryset.filter(user_id__isnull=True)
        return queryset


class ToyClubAssignView(LoginRequiredMixin, generic.UpdateView):
    model = ToyClub
    fields = ["user"]
    template_name = "toyshop/customers/toy_club_assign.html"
    success_url = reverse_lazy("customers:toy-club-list")

    def post(self, request, *args, **kwargs):
        if "confirm" in request.POST:
            return super().post(request, *args, **kwargs)

        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        user_id = self.request.POST.get("club_to_user")
        if user_id:
            form.instance.user_id = user_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club_to_user = self.request.GET.get("club_to_user") or self.request.POST.get("club_to_user")
        context["club_to_user"] = club_to_user
        return context
