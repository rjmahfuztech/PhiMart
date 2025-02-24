from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers,CategorySerializers
from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializers(data=request.data) # Deserializer
        # if serializer.is_valid():
        #     print(serializer.validated_data)
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save as if else before
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        copy_of_product = product
        product.delete()
        serializer = ProductSerializers(copy_of_product)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def view_category(request):
    if request.method == 'GET':
        category = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializers(data=request.data) # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializers(category)
    return Response(serializer.data)
