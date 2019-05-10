from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Product, Member, Benefit

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Benefit)
