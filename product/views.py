from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review, ProductImage
from product.serializers import ProductSerializer,CategorySerializer, ReviewSerializer, ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadOnly

# Create your views here.

'''All in one using (ModelViewSet) [create, read, update, delete]'''
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'updated_at']
    permission_classes = [IsAdminOrReadOnly]

    
    '''for specif customization if needed'''
    # def destroy(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     if product.stock > 5:
    #         return Response({'message': 'Product with stock more then 5 can not be deleted.'})
    #     self.perform_destroy(product)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_pk'])


'''All in one using (ModelViewSet) [create, read, update, delete]'''
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}