from django.contrib import admin
from .models import BasketProduct, Basket


admin.site.register(Basket)
admin.site.register(BasketProduct)
