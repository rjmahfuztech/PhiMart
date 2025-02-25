from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.category_urls'))
# ]
