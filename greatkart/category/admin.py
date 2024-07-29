from django.contrib import admin
from .models import Category

# Register your models here.    

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # Ajoutez une virgule ici
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)

