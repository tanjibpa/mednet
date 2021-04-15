from django.contrib.auth.models import User

from organization.models import Organization


def has_organization(user: User) -> Organization:
    try:
        organization = Organization.objects.get(user=user)
        return organization
    except Organization.DoesNotExist:
        return None
