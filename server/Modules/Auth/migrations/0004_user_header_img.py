# Generated by Django 2.2.4 on 2019-11-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_auto_20191028_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='header_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]