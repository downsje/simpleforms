from project.forms import CustomerForm
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Customer
from django.contrib import messages

import json


# Create your views here.
def index(request):
    """
    Retrieves the customer form. 
    """
    # if a get, return a blank form
    form = CustomerForm()
    return render(request, 'project/index.html', {'form': form})


def customer_form(request):
    """
    Handles post of customer form
    """

    if request.method == "POST":
        form = CustomerForm(request.POST)
        data = {}
        if form.is_valid():
            data['error'] = ""
            data['customer_name'] = form.cleaned_data['customer_name']
            data['email_address'] = form.cleaned_data['email_address']
            data['subscription_type'] = form.cleaned_data['subscription_type']
            customer = Customer.objects.create(customer_name=data['customer_name'])
            customer.email_address = data['email_address']
            customer.subscription_type = data['subscription_type']
            customer.save()

            return JsonResponse(data)

        else:
            data['error'] = "The data entered was not valid"
            return JsonResponse(data)

    else:
        form = CustomerForm()
        return render(request, 'index.html', {'form': form})


def customer_list(request):
    """
    Retrieves a list of all customers for the customer grid
    """

    customerlist = []

    customers = Customer.objects.all()
    for c in customers:
        customerlist.append({
            'fields': {
                'customer_name': c.customer_name,
                'subscription_type': c.subscription_type,
                'email_address': c.email_address

            }
        })

    data = json.dumps(customerlist)
    return HttpResponse(data, content_type='application/json', status=200)
