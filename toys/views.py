from django.urls import reverse
from django.views import generic

from toys.models import Toy, Category


class HomePageView(generic.ListView):
    template_name = "toyshop/index.html"
    # paginate_by = 8

    def get_queryset(self):
        return Toy.objects.order_by("-updated_at")[:8]


class CategoryListView(generic.ListView):
    model = Category


class ToyListView(generic.ListView):
    model = Toy
    template_name = "toyshop/toys/toy_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Toy.objects.prefetch_related("category")

class ToyCreateView(generic.CreateView):
    model = Toy

    def get_success_url(self):
        return reverse("toys:toy-detail", kwargs={"pk": self.object.pk})


class ToyUpdateView(generic.UpdateView):
    model = Toy
    template_name = "toyshop/toys/toy_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("toys:toy-detail", kwargs={"pk": self.object.pk})


class ToyDetailView(generic.DetailView):
    model = Toy
    template_name = "toyshop/toys/toy_detail.html"
