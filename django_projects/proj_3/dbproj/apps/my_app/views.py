from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'my_app/index.html')