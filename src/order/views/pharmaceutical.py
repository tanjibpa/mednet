from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView, CreateView

from inventory.models import RawMaterial
from order.forms import OrderForm
from order.models import RawMaterialOrder


class PharmaceuticalRawMaterialOrderCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    permission_required = ("order.pharma_can_create_order_raw_material",)
    success_url = reverse_lazy("pharmaceutical_order:order_list_view")
    form_class = OrderForm
    template_name = "order/pharma/create.html"

    # def form_invalid(self, form):
    #     # print(form.errors)
    #     return super().form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.total_price = self.object.quantity * self.object.raw_material.price
        self.object.supplier = self.object.raw_material.supplier
        self.object.created_by = self.request.user
        return super().form_valid(form)


class PharmaceuticalRawMaterialOrderListView(
    LoginRequiredMixin, PermissionRequiredMixin, ListView
):
    model = RawMaterialOrder
    template_name = "order/pharma/lists.html"
    context_object_name = "orders"
    permission_required = ("order.pharma_can_view_ordered_raw_material",)

    def get_queryset(self):
        return RawMaterialOrder.objects.filter(created_by=self.request.user)
