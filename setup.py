#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-bootstrap',
    version = '2.1',
    description = 'Use Twitter\'s Bootstrap CSS framework to build your app. All the views Bambu uses all extend a base template which you create, that can be based on a skeleton Bootstrap template. Shortcut tags let you easily add breadcrumb trails and icons to your apps.',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'http://pypi.python.org/pypi/bambu-bootstrap',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
    install_requires = [
        'Django>=1.4',
        'django-bower'
    ],
    packages = [
        'bambu_bootstrap',
        'bambu_bootstrap.templatetags'
    ],
    package_data = {
        'bambu_bootstrap': [
            'static/bootstrap/css/*.css',
            'static/bootstrap/js/*.js',
            'static/bootstrap/fonts/*.*',
            'templates/bootstrap/*.html',
            'templates/search/*.html',
            'templates/*.html'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)
