from django.urls import path

from organization.views import (
    OrganizationCreateView,
    OrganizationDetailView,
    OrganizationEditView,
)

app_name = "organization"
urlpatterns = [
    path("", OrganizationCreateView.as_view(), name="organization_form_view"),
    path("edit", OrganizationEditView.as_view(), name="organization_edit_view"),
    path("details", OrganizationDetailView.as_view(), name="organization_details_view"),
]
