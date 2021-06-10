from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from inventory.models import Product
from order.forms import ProductOrderForm
from order.models import ProductOrder


class RetailerOrderProduct(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ProductOrderForm
    template_name = "order/retailer/create.html"
    success_url = reverse_lazy("retailer_order:order_list_view")
    permission_required = ("order.retailer_create_order",)

    # def form_invalid(self, form):
    #     print(form.errors)
    #     return super().form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.producer = self.object.product.producer
        return super().form_valid(form)


class RetailerOrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "order/retailer/lists.html"
    model = ProductOrder
    context_object_name = "orders"
    permission_required = ("order.retailer_order_list",)

    def get_queryset(self):
        return ProductOrder.objects.filter(created_by=self.request.user)
