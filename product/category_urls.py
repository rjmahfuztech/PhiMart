from django.urls import path
from product import views

urlpatterns = [
    path('', views.CategoryListCrateView.as_view(), name='category-list'),
    path('<int:pk>/', views.ViewSpecificCategory.as_view(), name='specific-category')
]