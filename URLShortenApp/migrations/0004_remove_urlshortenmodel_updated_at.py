# Generated by Django 3.2.7 on 2021-09-23 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLShortenApp', '0003_alter_urlshortenmodel_short_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortenmodel',
            name='updated_at',
        ),
    ]
