from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from inventory.models import Product
from order.forms import ProductOrderForm


class RetailerOrderProduct(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ProductOrderForm
    template_name = "order/retailer/create.html"
    success_url = reverse_lazy("pharmaceutical_order:order_list_view")
    permission_required = ("order.retailer_create_order",)

    def form_valid(self, form):
        return super().form_valid(form)
