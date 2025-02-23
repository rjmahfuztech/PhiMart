from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers,CategorySerializers
from django.db.models import Count

# Create your views here.
@api_view()
def view_products(request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializers(products, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def view_specific_product(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)


@api_view()
def view_category(request):
    category = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializers(category, many=True)
    return Response(serializer.data)

@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializers(category)
    return Response(serializer.data)
