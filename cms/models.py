# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django.db.models import signals
from common.appenginepatch.ragendja.dbutils import cleanup_relations
from django.core.urlresolvers import reverse
from cms.fields import CKEditor
from django.contrib.sites.models import Site

class Category(db.Model):
    
    name    =   db.StringProperty(required=True)
    code    =   db.StringProperty(required=True)
    
    order   =   db.IntegerProperty()
    
    def __unicode__(self):
        return u"%s %s (%s)" % (self.order, self.name, self.code)    
    
    class Meta:
        verbose_name = _('kategoria')
        verbose_name_plural = _('kategorie')
    
class Page(db.Model):
    
    title           =   db.StringProperty(required=True)
    url             =   db.StringProperty(required=False)
    code            =   db.StringProperty(required=False)
    template_name   =   db.StringProperty(required=False)
    
    stub            =   db.TextProperty()
    content         =   db.TextProperty()
    order           =   db.IntegerProperty(required=False)
    
    date_added      =   db.DateTimeProperty(auto_now=True)
    
    category        =   db.ReferenceProperty(Category, required=False, collection_name="pages_set")
    
    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return reverse('cms_page', kwargs={'page_key':self.id})
    
    def __unicode__(self):
        if self.category:
            return u"%s : %s" % (self.category, self.title)
        else:
            return u"%s" % (self.title)
    
    class Meta:
        verbose_name = _('strone')
        verbose_name_plural = _('strony')
        
        
        
        
          
        
class Section(db.Model):
    
    code        =   db.StringProperty()
    content     =   db.TextProperty()
    
    def __unicode__(self):
        return u"%s" % (self.code)    
    
    class Meta:
        verbose_name = _('sekcja')
        verbose_name_plural = _('sekcje')  
      
    
signals.pre_delete.connect(cleanup_relations, sender=Page)