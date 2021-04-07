from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    return render(request, 'accounts/dashboard.html', {'customers': customers})


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')
