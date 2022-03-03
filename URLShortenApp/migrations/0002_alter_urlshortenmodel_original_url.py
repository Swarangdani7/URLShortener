# Generated by Django 3.2.6 on 2021-08-30 19:33

import URLShortenApp.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLShortenApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortenmodel',
            name='original_url',
            field=models.CharField(max_length=150, validators=[URLShortenApp.forms.ValidateURL]),
        ),
    ]