from django.shortcuts import render
from .models import Petshop
# Create your views here.
def showproduct(request):
    shop = Petshop.objects.all()

    context = {
        'all_products': shop
    }
    return render(request, 'PetShop/productlist.html', context)
