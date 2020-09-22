from django import template

from articles.models import Elements, Section

register = template.Library()


@register.filter
def reformation(word):
    sec = Section.objects.prefetch_related("articles").filter(articles=word)

    # elem = Elements.objects.prefetch_related('section').filter(article__title=word).values_list('id', flat=True)

    return sec

