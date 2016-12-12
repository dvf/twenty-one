import datetime

from django import template
from django.utils import timezone


register = template.Library()


@register.filter(is_safe=True)
def weekday(offset):
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = timezone.now().today()
    offset = today + datetime.timedelta(days=offset)
    return day[offset.weekday()]

