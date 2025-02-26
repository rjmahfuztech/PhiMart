from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer,CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

# Create your views here.

'''All in one using (ModelViewSet) [create, read, update, delete]'''
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # for specif customization if needed
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 5:
            return Response({'message': 'Product with stock more then 5 can not be deleted.'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


'''All in one using (ModelViewSet) [create, read, update, delete]'''
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}