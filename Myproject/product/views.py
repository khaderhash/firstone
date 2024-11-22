from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .models import Product  


@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.all()
    print(products)
    return Response({"khh":"hhh"})