from django.contrib import admin
from .models import Info
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class InfoResource(resources.ModelResource):
    class Meta:
        model = Info
        skip_unchanged = True
        report_skipped = False
        fields = (
            'ism',
            'familya',
            'sharif',
            'jins',
            'tsana',
            'tuman',
            'manzil',
            'email',
            'telefon',
            'passport',
            'rasm',
            'iib',
            'pass_time',
            'anketa',
            'taqdimot_pdf',
            'loyiha_nomi',
            'faloliyat_turi',
            'st_mazmun',
            'st_ahamiyat',
            'st_dolzarb',
            'yangi_ishchi',
            'mijozlar',
            'raqobatchilar',
            'mablag',
            'st_natija',
            'malumot',
            'created',
            'natija',
            )

@admin.register(Info)
class InfoAdmin(ImportExportModelAdmin):
    list_display = ('ism','familya', 'loyiha_nomi', 'anketa','taqdimot_pdf', 'created',)
    list_filter = ('ism','jins','tuman','faloliyat_turi','created')
    search_fields = ('ism','familya','tuman','email','loyiha_nomi')
    resource_class = InfoResource

