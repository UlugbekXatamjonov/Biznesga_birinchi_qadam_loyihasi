from django.forms import ModelForm
from .models import Info
from django.contrib.auth.forms import UserCreationForm

class InfoForm(ModelForm):
	class Meta:
		model = Info
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
			'malumot'
			)

