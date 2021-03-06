"""HelloPaw_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views as userviews
from Home import views as home_views
from PetShop import views as product_views
from Payment import views as payment_views
from Petservice import views as service_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', userviews.showCustomer),
    path('', home_views.show_home),
    path('about/', home_views.show_about),
    path('shop/',product_views.showproduct),
    path('payment/',payment_views.showPayment),
    path('service/', service_views.show_service)
]
