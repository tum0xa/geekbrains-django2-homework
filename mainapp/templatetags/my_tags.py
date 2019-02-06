from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('mainapp/include/stars.html')
def show_ratting(ratting):
    one = "fa fa-star"
    half = "fas fa-star-half-alt"
    zero = "far fa-star"
    digit_list = ['zero', 'one', 'two', 'three', 'four', 'five']
    context = {
        'one': zero,
        'two': zero,
        'three': zero,
        'four': zero,
        'five': zero
    }

    int_rat = int(ratting)
    frac_rat = ratting - int_rat
    for i in range(1, len(context)+1):
        if i <= int_rat:
            context.update({digit_list[i]: one})
        elif i-int_rat == 1 and frac_rat != 0:
            context.update({digit_list[i]: half})
        else:
            context.update({digit_list[i]: zero})
    return context


if __name__ == '__main__':
    print(show_ratting(1.5))

