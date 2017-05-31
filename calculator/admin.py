from django.contrib import admin
from .models import Currency

# Register your models here.


@admin.register(Currency)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['Наименование', 'Код', 'За_единица', 'Лева']
