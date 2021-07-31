from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from product.forms import CategoryForm, SubCategoryForm, ProductForm
from product.models import Product, Category, SubCategory


class ProductView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product/product_list.html'


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_edit.html'
    success_url = reverse_lazy('product_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product_list')


class ProductListBySubCategoryView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product/product_list.html'


    def get_queryset(self):
        return Product.objects.filter(sub_category__slug=self.kwargs['slug'])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'category/category_list.html'


class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_edit.html'
    success_url = reverse_lazy('category_list')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class SubCategoryListView(ListView):
    model = SubCategory
    context_object_name = 'sub_category_list'
    template_name = 'subcategory/sub_category_list.html'
    paginate_by = 10

class SubCategoryListByCategoryView(ListView):
    model = SubCategory
    context_object_name = 'sub_category_list'
    template_name = 'subcategory/sub_category_list.html'


    def get_queryset(self):
        return SubCategory.objects.filter(category__slug=self.kwargs['slug'])


class SubCategoryEditView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'subcategory/sub_category_edit.html'
    success_url = '/sub_category_list/'


class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'subcategory/sub_category_confirm_delete.html'
    success_url = '/sub_category_list/'


class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'subcategory/sub_category_create.html'
    success_url = '/sub_category_list/'
