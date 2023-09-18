# Create a custom template tag file (e.g., myapp/templatetags/message_tags.py)
from django import template

register = template.Library()


@register.simple_tag
def message_theme(tag):
    # Map message tags to CSS classes
    css_classes = {
        'success': 'alert-green',
        'warning': 'alert-amber',
        'error': 'alert-red',
        'info': 'alert-indigo'
    }

    # Get the CSS class based on the message tag or default to 'info-message'
    css_class = css_classes.get(tag, 'info-message')

    return css_class
