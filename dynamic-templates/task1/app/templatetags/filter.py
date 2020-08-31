from django import template
from datetime import datetime

register = template.Library()


@register.filter
def str_to_int(word):
    return int(word)


@register.filter
def str_to_float(word):
    try:
        if len(word) == 1:
            return int(word)
        else:
            return float(word)
    except ValueError:
        return "-"



