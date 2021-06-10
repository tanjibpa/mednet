from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from inventory.forms import ProductForm
from inventory.forms.batch import BatchForm
from inventory.models import Product, RawMaterial, Batch

import logging

logger = logging.getLogger(__name__)

class PharmaProductsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "inventory/pharma/list.html"
    context_object_name = "products"
    paginate_by = 10
    permission_required = ("inventory.pharma_can_view_list",)

    def get_queryset(self):
        print(self.request.organization)
        return Product.objects.filter(producer=self.request.organization)


class PharmaProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = "inventory/pharma/create.html"
    form_class = ProductForm
    permission_required = ("inventory.pharma_can_create",)

    def get_success_url(self):
        return reverse_lazy(
            "pharma_inventory:product_detail_view", kwargs={"pk": self.object.id}
        )

    def form_valid(self, form):
        logger.info("form valid called")
        self.object = form.save(commit=False)
        self.object.producer = self.request.organization
        return super().form_valid(form)


class PharmaProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "inventory/pharma/update.html"
    form_class = ProductForm
    queryset = Product.objects.all()
    permission_required = ("inventory.pharma_can_update",)

    def get_success_url(self):
        return reverse_lazy(
            "pharma_inventory:product_detail_view", kwargs={"pk": self.object.id}
        )


class PharmaProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = "inventory/pharma/detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"
    permission_required = ("inventory.pharma_can_view",)


class PharmaRawMaterialListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = RawMaterial
    template_name = "inventory/pharma/raw_material_list.html"
    queryset = RawMaterial.objects.all()
    context_object_name = "raw_materials"
    permission_required = ("inventory.pharma_can_view_raw_material_list",)


class PharmaRawMaterialDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = RawMaterial
    template_name = "inventory/pharma/raw_material_detail.html"
    queryset = RawMaterial.objects.all()
    context_object_name = "raw_material"
    permission_required = ("inventory.pharma_can_view_raw_material",)


class PharmaBatchCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Batch
    form_class = BatchForm
    template_name = "inventory/pharma/create_batch.html"
    queryset = Batch.objects.all()
    # context_object_name = "batches"
    permission_required = ("inventory.pharma_can_create_batch",)

    def get_success_url(self):
        return reverse_lazy(
            "pharma_inventory:batch_detail_view", kwargs={"pk": self.object.id}
        )


class PharmaBatchDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Batch
    template_name = "inventory/pharma/batch_detail.html"
    queryset = Batch.objects.all()
    context_object_name = "batch"
    permission_required = ("inventory.pharma_can_view_batch",)


class PharmaBatchListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Batch
    queryset = Batch.objects.all()
    template_name = "inventory/pharma/batch_list.html"
    context_object_name = "batches"
    permission_required = ("inventory.pharma_can_view_batch",)
