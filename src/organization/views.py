from django.forms import Form
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from organization.forms import OrganizationForm
from organization.models import Organization


class OrganizationCreateView(CreateView):
    template_name = 'organization/organization.html'
    form_class = OrganizationForm
    success_url = reverse_lazy('organization:organization_details_view')

    def form_valid(self, form: Form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class OrganizationEditView(UpdateView):
    template_name = 'organization/organization_edit.html'
    form_class = OrganizationForm
    success_url = reverse_lazy('organization:organization_details_view')

    def get_object(self, queryset=None):
        return Organization.objects.get(user=self.request.user)


class OrganizationDetailView(TemplateView):
    template_name = 'organization/details.html'

    def get_queryset(self):
        return Organization.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        if not self.get_queryset():
            return redirect(reverse_lazy('organization:organization_form_view'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organization'] = self.get_queryset()[0]
        return context
