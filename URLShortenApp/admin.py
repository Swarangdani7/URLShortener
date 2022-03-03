from django.contrib import admin
from .models import URLShortenModel

# Register your models here.
class ShortenAdminModel(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'short_code', 'created_at')


admin.site.register(URLShortenModel, ShortenAdminModel)
