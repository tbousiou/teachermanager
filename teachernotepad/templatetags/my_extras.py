from django import template

register = template.Library()

@register.filter
def attendace_color_class(state):
    """
        state: True or False
    """
    if state:
        return "text-success"
    else:
        return "text-danger"