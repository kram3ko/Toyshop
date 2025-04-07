from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views import generic

from toys.forms import ToyCreateForm, ToySearchForm
from toys.models import Toy, Category


class HomePageView(generic.ListView):
    template_name = "toyshop/index.html"

    def get_queryset(self):
        return Toy.objects.order_by("-updated_at")[:8]

class ToyListView(generic.ListView):
    template_name = "toyshop/toys/toy_list.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = Toy.objects.prefetch_related("category")

        category_id = self.request.GET.get("category")
        if category_id:
            return queryset.filter(category__id=category_id).distinct()

        form = ToySearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                Q(name__icontains=form.cleaned_data["toy"]) |
                Q(description__icontains=form.cleaned_data["toy"]) |
                Q(manufacturer__icontains=form.cleaned_data["toy"])
            )

        return queryset

class ToyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Toy
    form_class = ToyCreateForm
    template_name = "toyshop/toys/toy_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("toys:toy-detail", kwargs={"pk": self.object.pk})


class ToyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Toy
    form_class = ToyCreateForm
    template_name = "toyshop/toys/toy_form.html"

    def get_success_url(self):
        return reverse("toys:toy-detail", kwargs={"pk": self.object.pk})


class ToyDetailView(generic.DetailView):
    model = Toy
    template_name = "toyshop/toys/toy_detail.html"


class ToyDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Toy
    template_name = "toyshop/toys/toy_confirm_delete.html"
    success_url = reverse_lazy("toys:toy-list")
