from django.contrib.auth.models import User
from django.http import HttpRequest

from organization.models import Organization


class SetOrganization:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_organization(user: User):
        return Organization.objects.filter(user=user).first()

    def __call__(self, request: HttpRequest):
        org = None
        if not request.user.is_anonymous:
            org = self.get_organization(request.user)
        setattr(request, 'organization', org)

        response = self.get_response(request)
        return response
