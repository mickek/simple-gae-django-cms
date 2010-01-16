from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

class CKEditor(forms.Textarea):

    class Media:
        js = (
            '/ckeditor/ckeditor.js',
            '/ckeditor/config.js',            
        )

    def __init__(self, *args, **kwargs):
        self.ck_attrs = kwargs.get('ck_attrs', {})
        if self.ck_attrs:
            kwargs.pop('ck_attrs')
        super(CKEditor, self).__init__(*args, **kwargs)

    def decompress(self):
        ck_attrs = ''
        if not 'language' in self.ck_attrs:
            self.ck_attrs['language'] = get_language()[:2]
        for k,v in self.ck_attrs.iteritems():
            ck_attrs += k + " : '" + v + "',"
        return ck_attrs

    def render(self, name, value, attrs=None):
        rendered = super(CKEditor, self).render(name, value, attrs)
        ck_attrs = self.decompress()
        return rendered + mark_safe(u'''<script type="text/javascript">
var CKeditor = new CKEDITOR.replace('id_%s',
{
customConfig : '',
%s
});
CKeditor.BasePath = "/ckeditor/";
</script>''' % (name, ck_attrs))

