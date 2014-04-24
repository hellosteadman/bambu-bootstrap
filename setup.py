#!/usr/bin/env python
from distutils.core import setup
from os import path

setup(
	name = 'bambu-bootstrap',
	version = '1.0',
	description = 'Frontend scaffolding thanks to Twitter\'s Bootstrap framework',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-bootstrap',
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	install_requires = [
		'Django>=1.4',
		'django-bower>=5.0.1'
	],
	namespace_packages = ['bambu'],
	packages = [
		'bambu.bootstrap',
		'bambu.bootstrap.templatetags'
	],
	package_data = {
		'bambu.bootstrap': [
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
