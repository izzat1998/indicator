from unidecode import unidecode

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from product.managers import CRUDManager


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_edit', args=[str(self.id)])


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    class Meta:
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('sub_category_edit', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(default='Опишите Продукт')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sub_category = models.ForeignKey(SubCategory, models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    objects = models.Manager()
    crud = CRUDManager()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse('product_detail', args=[str(self.id)])
