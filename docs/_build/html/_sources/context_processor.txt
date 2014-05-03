Context processor
=================

Bambu Bootstrap has a context processor that returns the current site, as defined in the Django sites framework.

Installation
------------

Add the following to your list of processors::

	bambu_bootstrap.context_processors.basics

Usage
-----

Use the ``SITE`` context variable to reference the current site's name or domain.