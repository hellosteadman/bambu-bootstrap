from django.template import Library
from django.conf import settings
from django.contrib.sites.models import Site

register = Library()
CSS_URL = getattr(settings, 'BOOTSTRAP_CSS_URL', '')
JS_URL = getattr(settings, 'BOOTSTRAP_JS_URL', '')

@register.inclusion_tag('bootstrap/styles.inc.html')
def bootstrap_styles():
    """
    Includes the Bootstrap styles from Bower
    """
    
    return {
        'css_url': CSS_URL and (settings.MEDIA_URL + CSS_URL) or ''
    }

@register.inclusion_tag('bootstrap/scripts.inc.html')
def bootstrap_scripts():
    """
    Includes the jQuery and Bootstrap scripts from Bower
    """
    
    return {
        'js_url': JS_URL and (settings.MEDIA_URL + JS_URL) or ''
    }

@register.inclusion_tag('bootstrap/navbar.inc.html', takes_context = True)
def bootstrap_navbar(context):
    """
    Renders the navbar template (see :ref:`Navigation templates <templates_navigation>`) for more information
    """
    
    context.update(
        {
            'INVERSE': getattr(settings, 'BOOTSTRAP_NAVBAR_INVERSE', False),
            'FIXED_TOP': getattr(settings, 'BOOTSTRAP_NAVBAR_FIXED_TOP', False),
            'FIXED_BOTTOM': getattr(settings, 'BOOTSTRAP_NAVBAR_FIXED_BOTTOM', False)
        }
    )
    
    return context

@register.inclusion_tag('bootstrap/footer.inc.html', takes_context = True)
def bootstrap_footer(context):
    """
    Renders the navbar template (see :ref:`Miscellaneous templates <templates_misc>`) for more information
    """
    
    return {
        'request': context.get('request'),
        'SITE': Site.objects.get_current()
    }

@register.simple_tag(takes_context = True)
def bootstrap_title(context, separator = ' | '):
    """
    Renders the value of the ``title_parts`` context variable (a tuple) into a string, separated by
    a delimiter
    
    :param separator: The delimiter to use (defaults to a beam character (|))
    """
    
    title_parts = context.get('title_parts')
    site = Site.objects.get_current()
    
    if title_parts:
        return u''.join(
            separator.join(
                [unicode(u) for u in list(title_parts) + [site.name]]
            )
        )
    else:
        return site.name

@register.inclusion_tag('bootstrap/breadcrumb.inc.html', takes_context = True)
def breadcrumb_trail(context):
    """
    Renders a two-tuple of page URLs and titles (see the
    :ref:`breadcrumb_trail <context_breadcrumb_trail>` context variable for more information)
    """
    
    return {
        'breadcrumb_trail': context.get('breadcrumb_trail')
    }

@register.simple_tag(takes_context = True)
def html_attrs(context):
    """
    Adds a ``no-js`` class to the ``<html>`` tag
    
    todo: Make this much more flexible
    """
    
    request = context.get('request')
    tags = [
        ('class', 'no-js')
    ]
    
    return ' '.join(
        ['%s="%s"' % t for t in tags]
    )

@register.inclusion_tag('bootstrap/typekit.inc.html')
def typekit():
    return {
        'key': getattr(settings, 'TYPEKIT_KEY', '')
    }