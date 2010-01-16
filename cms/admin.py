# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.models import Page, Category, Section
from cms.fields import CKEditor
from google.appengine.ext import db

class PageAdmin(admin.ModelAdmin): 
    
    formfield_overrides = {
        db.TextProperty: {'widget' : CKEditor(ck_attrs={'toolbar' : 'Custom'})},   
    }
    
    fieldsets = (
           (None, {
               'fields': ('title','url','category',)
           }),
           ('Treść',{
                'classes': ('collapse',),
                'fields': ('stub','content',)
           }),
           ('Zaawansowane', {
               'classes': ('collapse',),
               'fields': ('code','template_name','order','date_added',)
           }),
       )    

           

admin.site.register(Category) #@UndefinedVariable
admin.site.register(Page,PageAdmin) #@UndefinedVariable
admin.site.register(Section) #@UndefinedVariable