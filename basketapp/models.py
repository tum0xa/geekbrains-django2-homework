from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    total = models.PositiveIntegerField(verbose_name='сумма',default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def subtotal(self):
        return int(self.quantity * self.product.price)



