from django.shortcuts import render


def show_home(request):
    return render(request, 'home/home.html')


def show_about(request):
    return render(request, 'home/about.html')