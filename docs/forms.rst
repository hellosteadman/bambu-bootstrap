Forms
=====

Date fields
-----------

Add ``bootstrap-datepicker`` to your ``BOWER_INSTALLED_APPS`` setting

Link up the CSS via the ``extra_head`` block::

    <link href="{% static 'bootstrap-datepicker/css/datepicker3.css' %}" rel="stylesheet" media="screen" />

And add the script via the ``javascript`` block::

    <script src="{% static 'bootstrap-datepicker/js/bootstrap-datepicker.js' %}"></script>

