# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^p/(?P<page_key>[a-zA-z0-9]+)/$', 'cms.views.page_by_key', name='cms_page'),                       
)
