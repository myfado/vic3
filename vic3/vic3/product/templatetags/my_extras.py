from django import template


register = template.Library()


def get_discount(value,arg):
    """
    This returnes discounted price!
    """
    return round(float(value) * ((100 - arg)*0.01),2)

register.filter('get_discount',get_discount)
