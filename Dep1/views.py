from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#when we want to just ahow this simple line of text without any html file
# def home(request):
#   return HttpResponse("Welcome to Medihub OPD")

def index(request):
    return render(request,'dep1/index.html')

def product(request):
    return render(request,'dep1/product.html')