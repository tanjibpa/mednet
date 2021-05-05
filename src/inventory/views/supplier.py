from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from inventory.forms.raw_material import RawMaterialForm
from inventory.models import RawMaterial


class SupplierRawMaterialCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = RawMaterial
    form_class = RawMaterialForm
    template_name = "inventory/supplier/create.html"
    success_url = reverse_lazy("supplier_inventory:raw_material_list_view")
    permission_required = ("inventory.supplier_can_create",)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = self.request.organization
        return super().form_valid(form)


class SupplierRawMaterialUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):
    model = RawMaterial
    form_class = RawMaterialForm
    template_name = "inventory/supplier/update.html"
    permission_required = ("inventory.supplier_can_update",)

    def get_success_url(self):
        raw_material = self.get_object()
        return reverse_lazy(
            "supplier_inventory:raw_material_detail_view",
            kwargs={"pk": raw_material.id},
        )


class SupplierRawMaterialDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = RawMaterial
    template_name = "inventory/supplier/detail.html"
    context_object_name = "raw_material"
    permission_required = ("inventory.supplier_can_view",)

    def get_queryset(self):
        return RawMaterial.objects.filter(supplier=self.request.organization)


class SupplierRawMaterialListView(
    LoginRequiredMixin, PermissionRequiredMixin, ListView
):
    model = RawMaterial
    template_name = "inventory/supplier/lists.html"
    context_object_name = "raw_materials"
    permission_required = ("inventory.supplier_can_view_list",)

    def get_queryset(self):
        return RawMaterial.objects.filter(supplier=self.request.organization)
