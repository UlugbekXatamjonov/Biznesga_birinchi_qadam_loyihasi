# Generated by Django 4.0.3 on 2022-03-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_info_iib_alter_info_anketa_alter_info_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='iib',
            field=models.CharField(max_length=250, verbose_name='Passport bergan IIB'),
        ),
    ]
