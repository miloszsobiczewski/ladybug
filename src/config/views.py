from django.shortcuts import render


def home(request):
    return render(request, "config/index.html")


def policy(request):
    return render(request, "config/policy.html")
