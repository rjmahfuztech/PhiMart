from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.IntegerField(required=False)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'category', 'price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)

