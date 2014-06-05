"""
A base view with a number of mixins are provided here, as well as a simple
template view that provides an easy ``extra_context`` property.
"""

from django.db.models.base import ModelBase
from django.contrib import messages
from django.forms import Form
from django.views.generic.base import TemplateView
from django.shortcuts import redirect as redirect_shortcut
from django.utils import functional

class ObjectMixin(object):
    """
    A view mixin that makes it easier to work with single object views, where
    the title and breadcrumb trail might be influenced by a common factor
    """

    def get_object(self, request, **kwargs):
        return None

    def get_form(self, request, **kwargs):
        return self.form_class(request.POST or None,
            instance = self.get_object(request, **kwargs)
        )

    def get_body_classes(self, obj, **kwargs):
        return super(ObjectMixin, self).get_body_classes(**kwargs)

    def get_menu_selection(self, obj, **kwargs):
        return super(ObjectMixin, self).get_menu_selection(**kwargs)

    def get_title_parts(self, obj, **kwargs):
        return super(ObjectMixin, self).get_title_parts(**kwargs)

    def get_breadcrumb_trail(self, obj, **kwargs):
        return super(ObjectMixin, self).get_breadcrumb_trail(**kwargs)

    def get_base_context(self, request, obj, **kwargs):
        context = {
            'body_classes': self.get_body_classes(obj, **kwargs),
            'menu_selection': self.get_menu_selection(obj, **kwargs),
            'title_parts': self.get_title_parts(obj, **kwargs),
            'breadcrumb_trail': self.get_breadcrumb_trail(obj, **kwargs)
        }

        if isinstance(self, FormMixin):
            # A hack, to mitigate the need for a specific ObjectFormMixin
            context['form'] = self.get_form(request, **kwargs)

        return context

    def get(self, request, **kwargs):
        obj = self.get_object(request, **kwargs)
        context = self.get_base_context(request, obj, **kwargs)
        context.update(
            self.get_context_data(**kwargs)
        )

        context.update(
            self.get_extra_context(request, **kwargs)
        )

        return self.render_to_response(context)

class BootstrapView(TemplateView):
    """
    A class-based view to be rendered via a Bootstrap template, providing
    ways to setup ``<body>`` tag classes, formula for the ``<title>`` tag,
    the breadcrumb trail and a key indicating the selected main navigation item
    item.
    """

    body_classes = ()
    """The classes to add to the ``<body>`` tag"""

    menu_selection = None
    """A key indicating the selected menu item"""

    title_parts = ()
    """An interable of phrases that are concatonated with a beam, to form the
    ``<title>`` tag of a page"""

    breadcrumb_trail = ()
    """An interable of tuples with the of the inner pair being the URL (or
    relative path) and the second being the 'name' of the item. The first item
    in the iterable should be the start of the breadcrumb trail"""

    def get_body_classes(self, **kwargs):
        return self.body_classes

    def get_menu_selection(self, **kwargs):
        return self.menu_selection

    def get_title_parts(self, **kwargs):
        return self.title_parts

    def get_breadcrumb_trail(self, **kwargs):
        return self.breadcrumb_trail

    def get_extra_context(self, request, **kwargs):
        return {}

    def get_base_context(self, request, **kwargs):
        """
        Sets up the base context for the templated view
        """

        return {
            'body_classes': self.get_body_classes(**kwargs),
            'menu_selection': self.get_menu_selection(**kwargs),
            'title_parts': self.get_title_parts(**kwargs),
            'breadcrumb_trail': self.get_breadcrumb_trail(**kwargs)
        }

    def get(self, request, **kwargs):
        context = self.get_base_context(request, **kwargs)

        context.update(
            self.get_context_data(**kwargs)
        )

        context.update(
            self.get_extra_context(request, **kwargs)
        )

        return self.render_to_response(context)

    def redirect(self, *args, **kwargs):
        return redirect_shortcut(*args, **kwargs)

class MessageMixin(object):
    """
    A view mixin that provieds a simple way to implement
    ``django.contrib.messages``. You can define messages for various labels
    ('info', 'success', 'warning', 'error') and send them via a simple
    function.
    """
    messages = {}

    def message(self, request, key):
        """
        Sends a message to a user
        """

        if key in ('success', 'info', 'warning', 'error'):
            fn = getattr(messages, key)
        else:
            fn = messages.info

        fn(request, self.messages[key])

class FormMixin(MessageMixin):
    """
    A view mixin that provides a form for saving data.
    """

    form_class = Form
    """The type of form (should inherit from ``django.forms.ModelForm`` or
    have a ``save()`` method)"""

    def get_form(self, request, **kwargs):
        """
        Instantiates the form
        """

        return self.form_class(request.POST or None)

    def get_base_context(self, request, **kwargs):
        context = super(FormMixin, self).get_base_context(request, **kwargs)
        context['form'] = self.get_form(request, **kwargs)
        return context

    def validate_form(self, request, form):
        """
        Checks that the form data is valid
        """

        return form.is_valid()

    def save_form(self, request, form):
        """
        Saves the form data and returns the saved object
        """

        return form.save()

    def redirect_success(self, request):
        """
        Redirects back to the currently-requested URL
        """

        return self.redirect('.')

    def post(self, request, **kwargs):
        form = self.get_form(request, **kwargs)
        if self.validate_form(request, form):
            obj = self.save_form(request, form)

            if 'success' in self.messages:
                self.message(request, 'success')

            if isinstance(obj, (str, unicode)) or hasattr(obj, 'get_absolute_url'):
                return redirect_shortcut(obj)

            return self.redirect_success(request)
        elif 'error' in self.messages:
            self.message(request, 'error')

        return self.get(request, **kwargs)

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
