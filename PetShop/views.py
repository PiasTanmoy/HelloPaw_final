from django.shortcuts import render
from .models import Petshop
# Create your views here.
def showproduct(request):
    shop = Petshop.objects.all()

    context = {
        'all_products': shop
    }
<<<<<<< Updated upstream
    return render(request, 'PetShop/productlist.html', context)
=======
    return render(request, 'shop/productlist.html', context)
>>>>>>> Stashed changes
