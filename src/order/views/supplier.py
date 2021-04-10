from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView

from inventory.models import Product
from order.models import Order


class SupplierOrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order/list.html'
    queryset = Order.objects.all()
    context_object_name = 'orders'
    permission_required = ('order.supplier_order_list',)
