from django.shortcuts import render
from .models import Payment
# Create your views here.
def showPayment(request):

    all_payment = Payment.objects.all()

    print(all_payment)

    context ={
        "test" : "this is comig from views",
        "payment" : all_payment
    }

    return render(request,'Payment/PaymentList.html',context)