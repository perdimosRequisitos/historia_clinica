from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Add user to 'pacientes' group
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # asignar grupo al usuario
            print(user)
            group = Group.objects.get(name="medicos")
            print(group)
            user.groups.add(group)

            return redirect("historia:index")
        # else:
        #     for error in form.errors:
        #         print(error)
        #         messages.error(request, f"{error}: {form.errors[error]}")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("historia:index")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form": form})


def profile(request):
    context = {}
    context["user"] = request.user
    print(request.user, type(request.user))

    return render(request, "accounts/profile.html")
