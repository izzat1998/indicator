from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.
from django.urls import reverse

from product.forms import CategoryForm
from product.models import Product, SubCategory, Category


class ProductTests(TestCase):

    def setUp(self):
        category = Category.objects.create(name='Test', slug='test')
        subcategory = SubCategory.objects.create(name='Test', slug='test', category=category)
        self.product = Product.objects.create(
            name='Macbook',
            brand='apple',
            description='something is very interesting',
            price=125,
            sub_category=subcategory,
            image='product_image/image.jpg'

        )

    def test_book_listing(self):
        self.assertEqual(f'{self.product.name}', 'Macbook')
        self.assertEqual(f'{self.product.brand}', 'apple')
        self.assertEqual(f'{self.product.description}', 'something is very interesting')
        self.assertEqual(self.product.price, 125.00)

    def test_book_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Products')
        self.assertTemplateUsed(response, 'product/product_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Update')
        self.assertTemplateUsed(response, 'product/product_edit.html')
