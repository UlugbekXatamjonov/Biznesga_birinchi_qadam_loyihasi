from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

TUMAN = (
    ('davlatobod','Davlatobod tumani'),
    ('namangan_sh','Namangan shahri'),
    ('namangan_t','Namangan tumani'),
    ('norin','Norin tumani'),
    ('mingbuloq','Mingbuloq tumani'),
    ('yangiqoʻrgʻon','Yangiqoʻrgʻon tumani'),
    ('kosonsoy','Kosonsoy tumani'),
    ('pop','Pop tumani'),
    ('toʻraqoʻrgʻon','Toʻraqoʻrgʻon tumani'),
    ('uychi','Uychi tumani'),
    ('uchqoʻrgʻon','Uchqoʻrgʻon tumani'),
    ('chortoq','Chortoq tumani'),
    ('chust','Chust tumani'),
)

JINS = (
	('erkak','Erkak'),
	('ayol','Ayol'),
)

LOYIHA = (
	('i_ch','ishlab chiqarish'),
	('savdo','savdo'),
	('xizmat_k',"hizmat ko'rsatish"),
	('boshqa','boshqa'),
) # tekshir

RAQOBATCHILAR= (
	('ha','Ha'),
	('yoq',"Yo'q"),
)

NATIJA= (
	('ha','Qabul qilindi'),
	('yoq',"Qabul qilinmadi"),
)

class Info(models.Model):
	# shahsiy malumotlar
	ism  = models.CharField(max_length = 100, verbose_name='Ism')
	familya  = models.CharField(max_length = 100, verbose_name='Familya')
	sharif  = models.CharField(max_length = 100, verbose_name='Sharif')
	jins = models.CharField(max_length=100, choices=JINS, verbose_name='Jins')
	tsana = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Tug'ilgan sana")
	tuman = models.CharField(max_length=100, choices=TUMAN, verbose_name='Tuman')
	manzil = models.CharField(max_length=250, verbose_name='Manzil')
	email = models.EmailField(max_length=100, verbose_name='Email')
	telefon = PhoneNumberField(verbose_name='Telefon raqam')
	passport = models.CharField(max_length=15, verbose_name='Passport seria raqami')
	rasm = models.ImageField(upload_to='passport_rasmi/%Y/%m/%d/', verbose_name='Passport rasmi')
	iib = models.CharField(max_length=250, verbose_name='Passport bergan IIB')
	pass_time = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Passport berilgan sana')
	
	# loyiha malumotlari
	anketa = models.FileField(upload_to='anketa/%Y/%m/%d/', verbose_name='Anketa')
	taqdimot_pdf = models.FileField(upload_to='taqdimot_pdf/%Y/%m/%d/', verbose_name='Taaqdimot')
	loyiha_nomi = models.CharField(max_length=150, verbose_name='Loyiha nomi') 
	faloliyat_turi = models.CharField(max_length=100, choices=LOYIHA, verbose_name='Faoliyat turi') 
	st_mazmun = models.CharField(max_length=250, verbose_name='Start up mazmuni') 
	st_ahamiyat = models.CharField(max_length=250, verbose_name='Start up ahamiyati')
	st_dolzarb  = models.CharField(max_length=250, verbose_name='Start up dolzarbligi') 				 
	yangi_ishchi = models.CharField(max_length=100, verbose_name='Yangi ishchi') 
	mijozlar = models.CharField(max_length=250, verbose_name='Mijozlar')
	raqobatchilar = models.CharField(max_length=100, choices=RAQOBATCHILAR , verbose_name='Raqobatchilar')
	mablag = models.CharField(max_length=100, verbose_name='Mablag') 
	st_natija = models.CharField(max_length=300, verbose_name='Start updan kozlangan  natija') 
	malumot = models.TextField(null=True, blank=True, verbose_name="Qo'shimcha malumot") 
	# Indigator
	natija = models.CharField(max_length=100, choices=NATIJA, default='yoq', verbose_name='Start upning yakuniy natijasi')
	# date
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.familya + " " + self.ism



