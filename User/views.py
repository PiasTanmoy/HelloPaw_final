from django.shortcuts import render
from .models import Customer
# Create your views here.
def showCustomer(request):

    all_customer = Customer.objects.all()

    print(all_customer)

    context ={
        "test" : "this is comig from views",
        "customer" : all_customer
    }

    return render(request,'User/CustomerList.html',context)