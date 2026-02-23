from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def home(request):
    return render(request, 'frontend/home.html')
# Create your views here.
