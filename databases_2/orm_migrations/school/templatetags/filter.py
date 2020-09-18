from django import template

register = template.Library()


@register.filter
def reformation(word):
    return word
