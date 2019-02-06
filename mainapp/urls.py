from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.products, name='all'),
    path('<category_slug>', mainapp.products, name='category_products'),
    path('<category_slug>/<product_slug>', mainapp.product, name='product_view'),


]
