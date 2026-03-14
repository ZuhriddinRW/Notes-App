from django.shortcuts import render


def home(request):
    return render(request, "notes.html")

def welcome(request):
    return render(request, "index.html")