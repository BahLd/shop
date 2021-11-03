from django.urls import path

from product.views import *
from .class_views import *

urlpatterns = [
    path('home/', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:product_id>/', DetailListView.as_view(), name='detail'),
    path('product/create/', product_create, name='product-create'),
    path('product/update/<int:product_id>/', product_update, name='product-update'),
    path('product/delete/<int:product_id>/', product_delate, name='product-delete'),
]
