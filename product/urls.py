from django.urls import path
from .views import ProductView, CategoryListView, CategoryEditView, CategoryCreateView, \
    CategoryDeleteView, SubCategoryListView, SubCategoryEditView, SubCategoryDeleteView, SubCategoryCreateView, \
    SubCategoryListByCategoryView, ProductCreateView, ProductListBySubCategoryView, ProductEditView

urlpatterns = [
    path('product_list/', ProductView.as_view(), name='product_list'),
    path('product_list/<int:pk>/', ProductEditView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product_list/<str:slug>/', ProductListBySubCategoryView.as_view(), name='product_by_sub_category'),
    # Category
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_list/<int:pk>/edit/', CategoryEditView.as_view(), name='category_edit'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    # Subcategory
    path('sub_category_list/', SubCategoryListView.as_view(), name='sub_category_list'),
    path('sub_category_list/<int:pk>/edit/', SubCategoryEditView.as_view(), name='sub_category_edit'),
    path('sub_category_list/<int:pk>/delete/', SubCategoryDeleteView.as_view(), name='sub_category_delete'),
    path('sub_category/create/', SubCategoryCreateView.as_view(), name='sub_category_create'),
    path('sub_category/create/', SubCategoryCreateView.as_view(), name='sub_category_create'),
    path('sub_category_list/<str:slug>/', SubCategoryListByCategoryView.as_view(), name='sub_category_by_category'),
]
