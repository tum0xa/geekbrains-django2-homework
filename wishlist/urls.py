from django.urls import path

import wishlist.views as wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist.view, name='view'),
    path('add/<pk>/', wishlist.wishlist_add, name='add'),
    path('remove/<pk>/', wishlist.wishlist_add, name='remove'),
    path('clear/', wishlist.clear, name='clear'),

]