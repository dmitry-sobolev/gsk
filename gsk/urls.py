from django.conf.urls import patterns, url
from gsk.views import RootView

urlpatterns = patterns('',
                       url(r'^$', RootView.as_view(), name='root'),
                       )
