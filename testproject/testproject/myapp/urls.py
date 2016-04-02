from bambu_bootstrap.decorators import body_classes
from testproject.myapp import views
from django.conf.urls import url

urlpatterns = (
    url(r'^$', body_classes(views.home, 'homepage', 'index')),
)
