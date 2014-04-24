# Bambu Bootstrap

Frontend scaffolding thanks to Twitter's [Bootstrap](http://twitter.github.com/bootstrap/)
framework.

## About Bambu Bootstrap

Bambu Bootstrap provides utility templates, tags and filters that leverage Bootstrap's layout
and functionality. It also uses Font-Awesome's naming conventions.

## Static files

Previous versions of Bambu Bootstrap (when it was part of a single repo) included copies of
jQuery, Bootstrap and Font-Awesome in its static directory.

The new approach is to use Bower for static file management, so you'll need to install and
configure that to use this app.

## Installation

Install the package (including [django-bower](https://github.com/nvbn/django-bower))
via Pip:

```
pip install bambu-bootstrap
```

Add it and `djangobower` to your `INSTALLED_APPS` list (see the
[django-bower documentation](http://django-bower.readthedocs.org/en/latest/) for instructions
on implementing Bower):

```python
INSTALLED_APPS = (
    ...
    'djangobower',
    'bambu.bootstrap'
)
```

Add `bootstrap` and `fontawesome` to your `BOWER_INSTALLED_APPS` list:

```python
BOWER_INSTALLED_APPS = (
    ...
    'bootstrap',
    'fontawesome'
)
```

Then install the frontend packages to your Bower components directory:

```
python manage.py bower install
```

## Basic usage

Bambu Bootstrap contains a template at `bootstrap/base.html` which will get you up and
running. It includes everything you need to create a base template. Either extend that
template in your own `base.html` file, override it or strip it for parts.

## Full documentation

Full documentation can be found at [ReadTheDocs](http://bambu-bootstrap.readthedocs.org/).

## Questions or suggestions?

Find me on Twitter (@[iamsteadman](https://twitter.com/iamsteadman))
or [visit my blog](http://steadman.io/).
