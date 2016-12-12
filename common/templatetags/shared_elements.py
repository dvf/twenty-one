from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.inclusion_tag('elements/nav-link.html')
def nav_link(name, route=None, outline=None, context="info", active=None):
    return {
        'name': name,
        'active': None if not active else active,
        'outline': None if not outline else outline,
        'context': context,
        'route': '#' if not route else reverse_lazy(route)
    }


@register.inclusion_tag('elements/nav-divider.html')
def nav_divider(name=None):
    return {
        'name': name
    }


@register.inclusion_tag('elements/link.html')
def link(name, route=None, classes=None):
    return {
        'name': name,
        'classes': classes,
        'route': '#' if not route else reverse_lazy(route)
    }


@register.inclusion_tag('elements/section-heading.html')
def section_heading(name, context=None):

    return {
        'name': name,
        'context': context
    }


@register.inclusion_tag('elements/card-day.html')
def card_day(day, context='primary', log_id=None, clickable=False):
    return {
        'day': day,
        'context': context,
        'log_id': log_id,
        'clickable': clickable
    }