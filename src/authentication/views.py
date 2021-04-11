from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from authentication.forms import RegisterForm, LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                if not request.organization:
                    return redirect(reverse('organization:organization_form_view'))

                org_type_redirects = {
                    'pharmaceutical': reverse('pharma_inventory:product_list_view'),
                    'supplier': reverse('supplier_inventory:raw_material_list_view'),
                }

                return redirect(org_type_redirects[str(request.organization.org_type)])
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
