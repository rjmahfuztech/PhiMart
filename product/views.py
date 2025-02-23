from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category

# Create your views here.
@api_view()
def view_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product_dict = {
            'id': product.id,
            'name': product.name,
            'price': product.price
        }
        return Response(product_dict)
    except Product.DoesNotExist:
        return Response({'message': 'Product does not exists!'}, status=status.HTTP_404_NOT_FOUND)

@api_view()
def view_category(request):
    return Response({"messages": 'Category'})
