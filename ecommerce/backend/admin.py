from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Rating)
admin.site.register(LoveList)
admin.site.register(IngredientsTag)
admin.site.register(Ingredients)
