from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, generic

from toys.models import Toy
from wishlists.models import WishList, WishListItem


class WishListDetailView(LoginRequiredMixin, generic.DetailView):
    model = WishList
    template_name = "toyshop/wishlist/wishlist_detail.html"

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user).prefetch_related(
            "items__toy", "items__toy__category"
        )

    def get_object(self, queryset=None):
        wishlist, created = WishList.objects.get_or_create(user=self.request.user)
        return wishlist


class AssignWishListView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        toy = get_object_or_404(Toy, pk=pk)

        wishlist, _ = WishList.objects.get_or_create(user=request.user)
        wish_list_item = WishListItem.objects.filter(wishlist=wishlist, toy=toy).first()

        if wish_list_item:
            wish_list_item.delete()
        else:
            WishListItem.objects.create(wishlist=wishlist, toy=toy)

        if request.htmx:
            return render(request, "includes/part_incl/wishlist.html")
        return redirect(request.POST.get("next", "/"))

class RemoveFromWishListView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        wish_list_item = get_object_or_404(
            WishListItem, pk=pk, wishlist__user=request.user
        )
        wish_list_item.delete()

        return redirect(request.POST.get("next", "/"))
