from django.forms import ModelForm, TextInput, ChoiceField, Select, ModelChoiceField, ImageField, Textarea

from product.models import Product, Category, SubCategory


class ProductForm(ModelForm):
    sub_category = ChoiceField(
        choices=[(subcategory.id, subcategory.name) for subcategory in SubCategory.objects.all()])

    class Meta:
        model = Product
        fields = ['name', 'brand', 'description', 'price', 'sub_category', 'image']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'sub_category': Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sub_category'] = ModelChoiceField(
            queryset=SubCategory.objects.all())


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class SubCategoryForm(ModelForm):
    category = ChoiceField(choices=[(category.id, category.name) for category in Category.objects.all()])

    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)
        self.fields['category'] = ModelChoiceField(
            queryset=Category.objects.all())
