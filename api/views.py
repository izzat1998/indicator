from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
from api.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from product.models import Category, SubCategory, Product


class CategoryListApiView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListByCategoryApiView(ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.filter(category__slug=self.kwargs['slug'])


class ProductListByCategoryApiView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(sub_category__slug=self.kwargs['slug'])


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApiView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
