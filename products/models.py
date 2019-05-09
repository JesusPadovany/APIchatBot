from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return "product: {} precio: $ {}".format(self.name, self.price)
    
class ProductImages(models.Model):
    description = models.CharField(max_length=300)
    product = models.ForeignKey(Product, related_name="product_images",on_delete=models.CASCADE)
    image = models.CharField(max_length=100)

    def getUrlImage():
        return '/static/img/products'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name="product_categories",on_delete=models.CASCADE)

    def __str__(self):
        return "category: {} description: $ {}".format(self.name, self.description)