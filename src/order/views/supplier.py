from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, RedirectView

from order.forms import OrderForm
from order.models import RawMaterialOrder


class SupplierOrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'order/supplier/lists.html'
    context_object_name = 'orders'
    permission_required = ('order.supplier_can_view_order_raw_material_list',)

    def get_queryset(self):
        raw_material_orders = RawMaterialOrder.objects.filter(supplier=self.request.organization)
        return raw_material_orders


class SupplierOrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'order/supplier/update.html'
    form_class = OrderForm
    permission_required = ('order.supplier_can_edit_order_raw_material',)

    def get_queryset(self):
        raw_material_orders = RawMaterialOrder.objects.filter(supplier=self.request.organization)
        return raw_material_orders


class SupplierOrderFulfillView(LoginRequiredMixin, PermissionRequiredMixin, RedirectView):
    permission_required = ('order.supplier_can_edit_order_raw_material',)

    def get_redirect_url(self, *args, **kwargs):
        order = RawMaterialOrder.objects.get(id=kwargs['order_id'])
        order.status = RawMaterialOrder.OrderStatus.FULFILLED
        order.save()
        return reverse_lazy('supplier_order:order_list_view')


class SupplierOrderRejectView(LoginRequiredMixin, PermissionRequiredMixin, RedirectView):
    permission_required = ('order.supplier_can_edit_order_raw_material',)

    def get_redirect_url(self, *args, **kwargs):
        order = RawMaterialOrder.objects.get(id=kwargs['order_id'])
        order.status = RawMaterialOrder.OrderStatus.REJECTED
        order.save()
        return reverse_lazy('supplier_order:order_list_view')

