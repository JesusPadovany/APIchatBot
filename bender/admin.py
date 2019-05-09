from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Reflection, Product, ProductImage

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Reflection)
admin.site.register(Product)
admin.site.register(ProductImage)
