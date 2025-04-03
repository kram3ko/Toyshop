from django.views import generic

from toys.models import Toy, Category


class HomePageView(generic.ListView):
    model = Toy
    template_name = "toyshop/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits
        context["count_toys"] = context["paginator"].count
        context["category"] = Category.objects.all()
        return context

    def get_queryset(self):
        return Toy.objects.all()

class CategoryListView(generic.ListView):
    model = Category


class ToyListView(generic.ListView):
    model = Toy
    template_name = "toyshop/toys/toy_list.html"

class ToyCreateView(generic.CreateView):
    model = Toy

class ToyUpdateView(generic.UpdateView):
    model = Toy
    template_name = "toyshop/toys/toy_form.html"
    fields = "__all__"

class ToyDetailView(generic.DetailView):
    model = Toy
    template_name = "toyshop/toys/toy_detail.html"


