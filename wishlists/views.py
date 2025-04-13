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


class AddToWishListView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        toy = get_object_or_404(Toy, pk=pk)

        wishlist, _ = WishList.objects.get_or_create(user=request.user)
        wish_list_item, created = WishListItem.objects.get_or_create(
            wishlist=wishlist, toy=toy
        )
        if not created:
            wish_list_item.quantity = F("quantity") + 1
        wish_list_item.save()

        if request.htmx:
            return render(request, "includes/part_incl/wishlist.html")
        return redirect(request.POST.get("next", "/"))


class RemoveFromWishListView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        wish_list_item = get_object_or_404(
            WishListItem, pk=pk, wishlist__user=request.user
        )
        toy_name = wish_list_item.toy.name
        messages.success(request, f"{toy_name} removed from your wishlist.")
        wish_list_item.delete()

        return redirect(request.POST.get("next", "/"))
