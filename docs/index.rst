Bambu Bootstrap
===============

Use Twitter's `Bootstrap <http://twitter.github.com/bootstrap/>`_ CSS
framework to build your app. All the views Bambu uses all extend a base
template which you create, that can be based on a skeleton Bootstrap
template. Shortcut tags let you easily add breadcrumb trails and icons
to your apps.

About Bambu Bootstrap
---------------------

Bambu Tools is a set of reusable Django apps and utility packages that
help prototyping and building web apps easier. To a degree, this starts
with the front-end scaffolding. Bambu Bootstrap provides a base template
along with a set of useful tags and filters that make building web apps
using this framework easier.

Installation
------------

Install the package via Pip:

::

    pip install bambu-bootstrap

Add it to your ``INSTALLED_APPS`` list and add Bootstrap and
Font-Awesome to your ``BOWER_INSTALLED_APPS`` list (see the
`django-bower
documentation <http://django-bower.readthedocs.org/en/latest/>`_) for
details on managing static files through Bower.

::

    INSTALLED_APPS = (
        ...
        'djangobower',
        'bambu_bootstrap'
    )

    BOWER_INSTALLED_APPS = (
        ...
        'bootstrap',
        'fontawesome'
    )

Remember to run ``python manage.py bower install`` and
``python manage.py collectstatic``.

Basic usage
-----------

Within your project, start with a template called ``base.html``. This
should extend the Bootstrap base template,, at ``bootstrap/base.html``.

Use the ``extra_head`` block to specify stylesheets or script tags that
must, by necessity live in the head of your document.

Use the ``content`` block for the main content of your page.

Use the ``javascript`` block to specify JavaScript that can run at the
very bottom of the page.

Questions or suggestions?
-------------------------

Find me on Twitter (@iamsteadman) or `visit my blog <http://steadman.io/>`_.

.. toctree::
   :maxdepth: 1
   
   templates
   context_variables
   views
   forms
   fontawesome
   context_processor
   decorators
   templatetags
   settings

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
