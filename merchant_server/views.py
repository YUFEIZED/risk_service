from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from merchant_server.models import Customer
import json
from merchant_server.algorithm import risk_assessment

def home(request):
    return render(request, 'home.html')

#Check customer credit when receive a purchase
def check_credit(request):
    try:
        _name = request.GET.get('customer_name')
        _purchase = request.GET.get('purchase_amount')
        selectCustomers = Customer.objects.filter(customer_name=_name)
        if selectCustomers.exists():
            customer = selectCustomers.first()
            res = {}
            res['Name'] = _name
            res['Purchase'] = _purchase
            res['Credit'] = customer.credit
            res['Success'] = risk_assessment(_purchase, customer.credit)
            return JsonResponse(res)
        return HttpResponseBadRequest("Customer not existed.")
    except Exception as e:
        return HttpResponseBadRequest("Unknown error. {}".format(e))

#Update the credit information
def update_credit(request):
    try:
        _name = request.POST.get('customer_name')
        _new_credit = request.POST.get('new_credit')
        selectCustomers = Customer.objects.filter(customer_name=_name)
        if selectCustomers.exists():
            customer = selectCustomers.first()
            customer.credit = _new_credit
            customer.save()
            return HttpResponse("Update credit Successful. The updated credit is {}".format(_new_credit))
        return HttpResponseBadRequest("Customer not existed.")
    except Exception as e:
        return HttpResponseBadRequest("Unknown error. {}".format(e))

#Register new customer
def add_customer(request):
    try:
        _name = request.POST.get('customer_name')
        _credit = request.POST.get('credit')
        selectCustomers = Customer.objects.filter(customer_name=_name)
        if not selectCustomers.exists():
            newCustomer = Customer(customer_name=_name, credit=_credit)
            newCustomer.save()
            return HttpResponse("Register Successful.")
        return HttpResponse("Customer already existed.")
    except Exception as e:
        return HttpResponseBadRequest("Unknown error. {}".format(e))    