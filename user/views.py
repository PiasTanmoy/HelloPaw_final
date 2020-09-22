from django.shortcuts import render
from .models import Customer
# Create your views here.
def showUsers(request):

    users = Customer.object.all()

    context = {
        'all_customers': users
    }

    return render(request, 'user/CustomerList.html',context)

