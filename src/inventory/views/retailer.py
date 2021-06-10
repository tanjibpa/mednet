from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from inventory.models import Product


class RetailerProductList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "inventory/retailer/product_list.html"
    context_object_name = "products"
    queryset = Product.objects.all()
    permission_required = ("inventory.retailer_can_view_list",)


class RetailerProductDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "inventory/retailer/product_detail.html"
    context_object_name = "product"
    queryset = Product.objects.all()
    permission_required = ("inventory.retailer_can_view_detail",)
