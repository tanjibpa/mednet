from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, UpdateView, DetailView

from inventory.forms import ProductForm
from inventory.models import Product


class ProductsListView(ListView):
    template_name = 'inventory/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(producer=self.request.organization)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'inventory/create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('inventory:product_detail_view', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.producer = self.request.organization
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'inventory/update.html'
    form_class = ProductForm
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse_lazy('inventory:product_detail_view', kwargs={'pk': self.object.id})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
