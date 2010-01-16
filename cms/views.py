# -*- coding: utf-8 -*-

from django.contrib.flatpages.models import FlatPage
from django.template import loader, RequestContext
from ragendja.dbutils import get_object_or_404 , get_object
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from cms.models import Page

DEFAULT_TEMPLATE = 'cms/default.html'

def render_page(request, f):
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.stub = mark_safe(f.stub)
    f.content = mark_safe(f.content)

    c = RequestContext(request, {
        'page': f,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, FlatPage, f.id)
    return response    

def cmspage(request, url):
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(Page, 'url =', url)

    return render_page(request, f)

def page_by_key(request, page_key):

    f = get_object_or_404(Page, page_key)

    return render_page(request, f)