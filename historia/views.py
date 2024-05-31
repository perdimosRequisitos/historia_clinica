from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


@login_required
def index(request: HttpRequest):
    return render(request, "historia/base.html")
