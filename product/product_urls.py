from django.urls import path
from product import views

urlpatterns = [
    path('<int:id>/', views.view_product, name='product-list'),
]
