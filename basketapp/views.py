from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket, BasketProduct
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket(request):
    content = {}
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        if basket:

            basket_products = BasketProduct.objects.filter(basket=basket[0])
            content = {'basket_items': basket_products,}
            content.update({"basket": basket[0]})
        else:
            basket = Basket(user=request.user)
            basket.save()
            basket_products = BasketProduct.objects.filter(basket=basket)
            content = {'basket_items': basket_products,}
            content.update({"basket": basket})
    categories = ProductCategory.objects.all()
    content.update({'category_list': categories})
    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk, quantity):
    quantity = int(quantity)
    content = {}
    product = Product.objects.get(pk=pk)
    basket = Basket.objects.filter(user=request.user)
    if basket:
        old_basket_item = BasketProduct.objects.filter(basket=basket[0], product=product)
        if old_basket_item:
            old_basket_item[0].quantity += quantity

            basket[0].total += old_basket_item[0].product.price*quantity
            old_basket_item[0].save()
        else:
            new_basket_item = BasketProduct(basket=basket[0], product=product)
            new_basket_item.quantity += quantity

            basket[0].total += new_basket_item.product.price*quantity
            new_basket_item.save()
        basket[0].quantity += quantity
        basket[0].save()
        basket = basket[0]
    else:
        new_basket = Basket(user=request.user)
        new_basket.quantity += quantity
        new_basket.save()
        new_basket_item = BasketProduct(basket=new_basket, product=product)
        new_basket_item.quantity += quantity
        new_basket.total += new_basket_item.product.price*quantity
        new_basket_item.save()
        new_basket.save()
        basket = new_basket
    if request.is_ajax():
        content = {
            'basket': basket,
        }
        basket_info = render_to_string('basketapp/inc_basket_info.html', content)
        return JsonResponse({
                      'basket_info': basket_info,
                      })
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def basket_remove(request,pk):

    if request.is_ajax():
        basket_item = BasketProduct.objects.get(pk=int(pk))
        basket_item.delete()
        basket_items = BasketProduct.objects.filter(basket__user=request.user)
        basket = Basket.objects.get(user=request.user)
        basket.quantity = 0
        basket.total = 0
        for item in basket_items:
            basket.quantity += item.quantity;
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
