from django import template

register = template.Library()

@register.filter
def discounted(value, arg):
    return value * (100-arg)/100

@register.filter
def mult(value, arg):
    return value * arg

@register.simple_tag
def mult_of_discon(price, discount, quantity):
    discon_price = price * (100-discount)/100
    return discon_price * quantity
