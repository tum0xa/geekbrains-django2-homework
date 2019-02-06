from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<pk>/<quantity>', basketapp.basket_add, name='add'),
    path('remove/<pk>/', basketapp.basket_remove, name='remove'),
    path('remove_single/<pk>/', basketapp.basket_remove_single, name='remove_single'),
    path('edit/<pk>/<quantity>', basketapp.basket_edit, name='edit'),
    # path('checkout/', basketapp.checkout, name='checkout')
]
