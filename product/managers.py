from django.db import models




class CRUDManager(models.Manager):
    def update_product(self, data, pk):
        product = self.get(pk=pk)
        product.name = data['name']
        product.brand = data['brand']
        product.description = data['description']
        product.price = data['price']
        product.sub_category_id = data['sub_category']
        product.save()
