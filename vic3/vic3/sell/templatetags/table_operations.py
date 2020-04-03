from django import template
import math

register = template.Library()

@register.filter
def discounted(value, arg):
    return int(math.ceil(value * (100-arg)/100))


@register.filter
def mult(value, arg):
    return int(math.ceil(value * arg))


@register.simple_tag
def mult_of_discon(price, discount, quantity):
    discon_price = int(math.ceil(price * (100-discount)/100))
    return discon_price * quantity
