# Generated by Django 2.1.7 on 2019-10-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20191028_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(default='', max_length=150),
        ),
    ]