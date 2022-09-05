from django import template
import datetime



register = template.Library()


@register.filter(name="TAG")
def cutter(value, arg):
    return value[:arg]


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

# register.filter("TAG", cutter)