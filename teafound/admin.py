from django.contrib import admin
from .models import Resource,Chemistry
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Chemistry
        verbose_name_plural = 'chemistryObejct'

admin.site.register(Resource)
admin.site.register(Chemistry)

