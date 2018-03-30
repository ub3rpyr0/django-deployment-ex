from django import template

register = template.Library()

@register.filter(name='cutt')
def cutt(value,arg):
    """
    This cuts out all values of "arg" from the string.
    It's named cutt instead of cut to avoid conflict with a built-in method.
    """
    return value.replace(arg,'')

# register.filter('cutt',cutt)
