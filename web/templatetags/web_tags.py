from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if filter:
        return CategoryCard.objects.all().order_by(filter)
    else:
        return CategoryCard.objects.all()


@register.simple_tag()
def get_tovars(filter=None):
    if filter:
        return Tovar.objects.all().order_by(filter)
    else:
        return Tovar.objects.all()

