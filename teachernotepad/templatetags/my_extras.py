from django import template

register = template.Library()

@register.filter
def attendace_color_class(state):
    """
        state: True or False
    """
    if state:
        return "link-success"
    else:
        return "link-danger"