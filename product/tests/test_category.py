from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from product.forms import CategoryForm
from product.models import  Category


class CategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Настольный компьютер")

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolute_url(), '/category_list/6/edit/')

    def test_category_content(self):
        self.assertEqual(f'{self.category.name}', 'Настольный компьютер')
        self.assertEqual(f'{self.category.id}', '1')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'List')
        self.assertTemplateUsed(response, 'category/category_list.html')

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_edit', args=(self.category.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update')
        self.assertTemplateUsed(response, 'category/category_edit.html')

    def test_category_create_form(self):
        name = "Новая какая та категория"
        data = {'name': name}
        form = CategoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_category_delete_view(self):
        response = self.client.post(
            reverse('category_delete', args=(self.category.id,)))
        self.assertEqual(response.status_code, 302)
