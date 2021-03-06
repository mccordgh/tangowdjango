from django.contrib import admin
from rango import models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Page, PageAdmin)