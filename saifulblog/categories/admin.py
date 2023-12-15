from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cat_name',)}
    list_display = ['cat_name', 'slug']

admin.site.register(models.Category, CategoryAdmin)