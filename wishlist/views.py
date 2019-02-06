from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from wishlist.models import WishlistProduct
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import login_required
from basketapp.models import Basket
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def view(request):
    content = {}
    if request.user.is_authenticated:
        wishlist_products = WishlistProduct.objects.filter(user=request.user)
        content = {'wishlist_items': wishlist_products, }

        wishlist_products_count = wishlist_products.count()
        content.update({'wishlist_products_count': wishlist_products_count})

        basket = Basket.objects.filter(user=request.user)
        content.update({'basket': basket})

    categories = ProductCategory.objects.all()
    content.update({'category_list': categories})

    return render(request, 'wishlist/wishlist.html', content)

@login_required
def wishlist_add(request, pk):
    content = {}
    product = Product.objects.get(pk=int(pk))
    # print(product)
    wishlist_product = WishlistProduct.objects.filter(product__pk=int(pk), user=request.user)
    if wishlist_product:
        wishlist_remove(request, pk)
    else:
        wishlist_product = WishlistProduct(product=product, user=request.user)
        wishlist_product.save()
    if request.is_ajax():
        wishlist_products_count = WishlistProduct.objects.filter(user=request.user).count()
        content.update({'wishlist_products_count': wishlist_products_count})
        wishlist_info = render_to_string('wishlist/inc_wishlist_info.html', content)
        return JsonResponse({
            'wishlist_info': wishlist_info,
        })
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def wishlist_remove(request, pk):
    content = {}

    if request.is_ajax():
        wishlist_item = WishlistProduct.objects.filter(product__pk=int(pk), user=request.user)
        print("я тут"+pk)
        if wishlist_item:
            wishlist_item[0].delete()
        wishlist_products_count = WishlistProduct.objects.filter(user=request.user).count()
        content.update({'wishlist_products_count': wishlist_products_count})
        wishlist_info = render_to_string('wishlist/inc_wishlist_info.html', content)
        wishlist_items = render_to_string('wishlist/wishlist.html', content)
        return JsonResponse({'wishlist_info': wishlist_info,
                         'wishlist_items': wishlist_items,
                         })
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def basket_remove_single(request, pk):

    if request.is_ajax():
        basket_item = BasketProduct.objects.get(pk=int(pk))
        if basket_item.quantity > 1:
            basket_item.quantity -= 1
            basket_item.save()
        else:
            basket_remove(request,pk);
        basket_items = BasketProduct.objects.filter(basket__user=request.user)
        basket = Basket.objects.get(user=request.user)
        basket.quantity = 0
        basket.total = 0
        for item in basket_items:
            basket.quantity += item.quantity
            basket.total += (item.subtotal())
        basket.save()
        content = {
            'basket_items': basket_items,
        }
        result = render_to_string('basketapp/inc_basket_items.html', content)

        content = {
            'basket': basket,
        }
        basket_info = render_to_string('basketapp/inc_basket_info.html', content)
        basket_total = render_to_string('basketapp/inc_basket_total.html', content)
    return JsonResponse({'result': result,
                         'basket_info': basket_info,
                         'basket_total': basket_total,
                         })

@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = BasketProduct.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()


        basket_items = BasketProduct.objects.filter(basket__user=request.user)

        content = {
            'basket_items': basket_items,
        }
        result = render_to_string('basketapp/inc_basket_items.html', content)

        basket = Basket.objects.get(user=request.user)
        basket.quantity = 0
        basket.total = 0
        for item in basket_items:
            basket.quantity += item.quantity
            basket.total += (item.subtotal())
        basket.save()
        content = {
            'basket': basket,
        }
        basket_info = render_to_string('basketapp/inc_basket_info.html', content)
        basket_total = render_to_string('basketapp/inc_basket_total.html', content)

        return JsonResponse({'result': result,
                             'basket_info': basket_info,
                             'basket_total': basket_total,
                             })



# def checkout(request):
#     content = {}
#     return render(request, 'mainapp/main.html', content)

def clear():
    pass