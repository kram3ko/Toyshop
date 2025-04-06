from django.db.models import Q
from django.urls import reverse
from django.views import generic

from toys.models import Toy, Category


class HomePageView(generic.ListView):
    template_name = "toyshop/index.html"

    def get_queryset(self):
        return Toy.objects.order_by("-updated_at")[:8]


class CategoryListView(generic.ListView):
    model = Category


class ToyListView(generic.ListView):
    model = Toy
    template_name = "toyshop/toys/toy_list.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = Toy.objects.prefetch_related("category")
        search_query = self.request.GET.get("q")
        category_id = self.request.GET.get("category")

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(manufacturer__icontains=search_query)
            )

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset.order_by("-updated_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["search_query"] = self.request.GET.get("q", "")
        context["selected_category"] = self.request.GET.get("category")
        return context

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
