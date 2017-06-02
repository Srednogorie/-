from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from .models import Currency
from . import bnb_currency_parser_two

# Register your models here.


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['Наименование', 'Код', 'За_единица', 'Лева']

    def get_urls(self):    # Include my_url in to the pool and define view
        urls = super(CurrencyAdmin, self).get_urls()
        urlpatterns = [
            url(r"^synchronize/$", synchronize)
        ]
        return urlpatterns + urls


@staff_member_required
def synchronize(request):
    bnb_currency_parser_two.parser()

    return HttpResponseRedirect('/admin/calculator/currency/') # Go back to the start



