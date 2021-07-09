from django.urls import path

from api.views import CategoryListApiView, SubcategoryListByCategoryApiView, ProductListByCategoryApiView, \
    ProductDetailApiView, ProductList

urlpatterns = [
    path('category_list/', CategoryListApiView.as_view(), name='category_list'),
    path('category_list/<str:slug>/', SubcategoryListByCategoryApiView.as_view(), name='sub_category_by_category'),
    path('sub_category_list/<str:slug>/', ProductListByCategoryApiView.as_view(),
         name='product_list_by_sub_category'),
    path('product_list/', ProductList.as_view(),
         name='product_list'),
    path('product_list/<int:id>/', ProductDetailApiView.as_view(),
         name='product_detail'),
]
