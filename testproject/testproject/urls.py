from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'^', include('testproject.myapp.urls'))
]

if settings.DEBUG:
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	urlpatterns += staticfiles_urlpatterns()
