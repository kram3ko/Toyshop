from django import template

register = template.Library()


@register.filter
def price_format(value):
    try:
        return f"{value / 100:.2f}"
    except (TypeError, ValueError):
        return ""
