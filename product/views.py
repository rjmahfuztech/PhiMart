from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers,CategorySerializers
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

# Create your views here.
@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializers(data=request.data) # Deserializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializers(data=request.data) # Deserializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductListCrateView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializers

    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()

    # def get_serializer_class(self):
    #     return ProductSerializers


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
    
class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
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
        
class ViewCategory(APIView):
    def get(self, request):
        category = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializers(data=request.data) # Deserializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryListCrateView(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_category(request, pk):
    category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=pk)
    
    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        copy_of_category = category
        category.delete()
        serializer = CategorySerializers(copy_of_category)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
class ViewSpecificCategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializers(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        copy_of_category = category
        category.delete()
        serializer = CategorySerializers(copy_of_category)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)