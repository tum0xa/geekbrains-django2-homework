from django.db import models
from django.conf import settings
from mainapp.models import Product


class WishlistProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)




