from django.urls import path
from product.views import get_products
from accounts.urls import *
urlpatterns = [
    path('<slug>/',get_products,name='get_products'),
]