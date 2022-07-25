from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_id', 'category_title')
    list_display_links = ('id', 'cat_id', 'category_title')
    search_fields = ('cat_id', 'category_title')
    prepopulated_fields = {'cat_id': ("category_title",)}

class TovarAdmin(admin.ModelAdmin):
    list_display = ('tovar_id', 'cat_id', 'tovar_title', 'tovar_price', 'tovar_discription')
    list_display_links = ('tovar_id', 'cat_id', 'tovar_title', 'tovar_price', 'tovar_discription')
    search_fields = ('tovar_id', 'cat_id', 'tovar_title', 'tovar_price', 'tovar_discription')
    list_filter = ('tovar_id', 'cat_id', 'tovar_price')
    prepopulated_fields = {'tovar_id': ("tovar_title",)}


admin.site.register(CategoryCard, CategoryAdmin)
admin.site.register(Tovar, TovarAdmin)
