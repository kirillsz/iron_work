from django.contrib import admin

from .models import *



class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'desc', 'created_at')  # Добавьте поле даты в список отображаемых полей
    search_fields = ['phone', 'desc']
    ordering = ['-created_at']  # Сортировка по убыванию даты создания

# Регистрируем модель с настройками
admin.site.register(Order, OrderAdmin)

40817810829002986316