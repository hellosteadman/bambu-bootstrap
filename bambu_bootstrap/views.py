from django.views.generic import TemplateView

class DirectTemplateView(TemplateView):
    """
    This is similar to Django's old direct template generic view. It's handiest when used for 'static'
    pages like homepages (ie: where dynamic data may come from context processors so a standard view
    isn't needed). It supports context variables via the ``extra_context`` argument.
    """
    
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        
        return context