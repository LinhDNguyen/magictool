from django.conf.urls.defaults import *

urlpatterns = patterns('notemanagement.views',
    (r'^$', 'index'),
)