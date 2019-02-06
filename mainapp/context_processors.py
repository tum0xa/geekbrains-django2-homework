from basketapp.models import Basket


def basket(request):

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if len(basket) > 0:
        basket = basket[0]
    return {'basket': basket}
