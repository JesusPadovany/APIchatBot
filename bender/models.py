from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text

class Reflection(models.Model):
    first_person = models.CharField(max_length=200)
    third_person = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='./static/img/products', default = 'none')

    def __str__(self):
        return "product: {} price: $ {}".format(self.name, self.price)

class ProductImage(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img/products', default = 'false')
    product = models.ForeignKey(Product, related_name="product_images",on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.description)
    


