from functools import wraps
from django.template.response import TemplateResponse
import logging

def body_classes(func, *classes):
    """
    Decorates a view by adding a list of class names to the ``<body>`` tag. The prefered way to use this
    is to pass in a view that returns a `TemplateResponse` object, so that the decorator can modify the
    context variable dictionary, adding a `body_classes` list, or extending it if it already exists.
    
    :param func: A callable that returns an ``HttpResponse`` or ``TemplateResponse`` object
    :param classes: A list of classes to add to the ``<body>`` tag
    
    Use this decorator in your URLconf like so::
    
        from bambu_bootstrap.decorators import body_classes
        from testproject.myapp import views
        from django.conf.urls import patterns, url
        
        urlpatterns = patterns('',
            url(r'^$', body_classes(views.home, 'homepage', 'index'))
        )
    """
    
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code != 200 or not any(classes):
            return response

        if not isinstance(response, TemplateResponse):
            logger = logging.getLogger('bambu_bootstrap')
            logger.warning(
                'body_classes decorator applied to incompatible view %s.%s. Falling back ' \
                'to dirty HTML injection' % (
                    func.__module__, func.__name__
                )
            )
            
            content = response.content
            body_start = content.find('<body')
            
            if body_start > -1:
                body_end = content.find('>', body_start + 1)
                
                if body_end > -1:
                    body = content[body_start:body_end]
                    class_start = body.find('class="')
                    if class_start > -1:
                        class_start += len('class="')
                        class_end = body.find('"', class_start)

                        if class_end > -1:
                            classlist = body[class_start:class_end].split(' ')
                            classlist.extend(classes)
                            classlist = ' '.join(
                                [c for c in classlist if c and c.strip()]
                            )

                            before_class = body_start + class_start
                            after_class = body_start + class_end

                            response.content = ''.join(
                                (
                                    content[:before_class],
                                    classlist,
                                    content[after_class:]
                                )
                            )
        else:
            if not response.context_data is None:
                body_classes = list(response.context_data.get('body_classes', []))
            else:
                body_classes = []
                response.context_data = {}
            
            body_classes.extend(classes)
            response.context_data['body_classes'] = body_classes

        return response

    return wrapped_func