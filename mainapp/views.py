from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import ProductCategory, Product, Banner, Company
from basketapp.models import Basket
from wishlist.models import WishlistProduct
import csv

def main(request):
    wishlist_products_count = 0
    popular_products = Product.objects.filter(ratting__in=[4, 4.5, 5])

    banners = Banner.objects.all()
    categories = ProductCategory.objects.all().filter(is_active=True)
    sales_list = Product.objects.filter(discount__in=[20, 25, 30, 40, 50])
    if not request.user.is_anonymous:
        wishlist_products_count = WishlistProduct.objects.filter(user=request.user).count()
    company = Company.objects.all()[0]
    content = {'products_popular': popular_products,
               'category_list': categories,
               'banners': banners,
               'company': company,
               'wishlist_products_count': wishlist_products_count,
               'sales_list': sales_list,
               }
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
    #     if basket:
    #         content.update({"basket": basket[0]})

    return render(request, 'mainapp/main.html', content)


def products(request, category_slug):
    wishlist_products_count = 0
    categories = ProductCategory.objects.all().filter(is_active=True)
    category = ProductCategory.objects.get(slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)
    if not request.user.is_anonymous:
        wishlist_products_count = WishlistProduct.objects.filter(user=request.user).count()
    content = {'products': products,
               'category_list': categories,
               'category': category,
               'wishlist_products_count': wishlist_products_count,
               }

    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
    #     if basket:
    #         content.update({"basket": basket[0]})
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def product(request, category_slug, product_slug):
    wishlist_products_count = 0
    product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    categories = ProductCategory.objects.all().filter(is_active=True)
    if not request.user.is_anonymous:
        wishlist_products_count = WishlistProduct.objects.filter(user=request.user).count()
    content = {'product': product,
               'category_list': categories,
               'wishlist_products_count': wishlist_products_count,}
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
    #     if basket:
    #         content.update({"basket": basket[0]})

    return render(request, 'mainapp/product.html', content)





