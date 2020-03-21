# Generated by Django 3.0.4 on 2020-03-20 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0018_registerngorequest_registered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='mobilpay_icc',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='mobilpay Merchant identifier code'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='mobilpay_private_key',
            field=models.FileField(blank=True, max_length=300, null=True, upload_to='', verbose_name='mobilpay Private key'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='mobilpay_public_key',
            field=models.FileField(blank=True, max_length=300, null=True, upload_to='', verbose_name='mobilpay Public key'),
        ),
    ]
