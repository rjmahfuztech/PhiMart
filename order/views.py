from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from order.serializers import CartSerializer
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from order.models import Cart, CartItem

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.prefetch_related('items__product').all()