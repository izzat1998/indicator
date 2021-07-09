from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from product.forms import CategoryForm, SubCategoryForm
from product.models import Category, SubCategory


class SubCategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Тест")
        self.subcategory = SubCategory.objects.create(name="Настольный компьютер", category=self.category)

    def test_get_absolute_url(self):
        self.assertEqual(self.subcategory.get_absolute_url(), '/sub_category_list/4/edit/')

    def test_subcategory_content(self):
        self.assertEqual(f'{self.subcategory.name}', 'Настольный компьютер')
        self.assertEqual(f'{self.subcategory.id}', '5')

    def test_subcategory_list_view(self):
        response = self.client.get(reverse('sub_category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'List')
        self.assertTemplateUsed(response, 'subcategory/sub_category_list.html')

    def test_subcategory_detail_view(self):
        response = self.client.get(reverse('sub_category_edit', args=(self.subcategory.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update')
        self.assertTemplateUsed(response, 'subcategory/sub_category_edit.html')

    def test_subcategory_create_form(self):
        name = "Новая какая та категория"
        data = {'name': name,
                'category': self.category}
        form = SubCategoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_subcategory_delete_view(self):
        response = self.client.post(
            reverse('sub_category_delete', args=(self.subcategory.id,)))
        self.assertEqual(response.status_code, 302)
