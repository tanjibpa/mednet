from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from inventory.models import Product
from order.models import Order


class PharmaceuticalOrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, RedirectView):
    permission_required = ('order.add_order',)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('seller_order:order_list_view')

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=int(self.kwargs['product_id']))
        Order.objects.create(created_by=self.request.user, product=product, producer=product.producer)
        return super().get(request, *args, **kwargs)
