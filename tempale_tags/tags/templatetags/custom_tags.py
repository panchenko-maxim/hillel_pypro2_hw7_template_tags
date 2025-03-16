from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date():
    return datetime.now().strftime("%Y-%m-%d")

@register.filter(name='truncate')
def truncate(value, length=10):
    if len(value) > length:
        return value[:length] + "..."
    return value

@register.inclusion_tag('tags/greeting.html')
def greeting(name):
    return {'name': name}