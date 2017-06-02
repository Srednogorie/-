from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from .models import Currency
from .forms import CurrencyForm

# Create your views here.

'''
def currencies_list_view(request):
    form = CurrencyForm
    currencies = Currency.objects.all()
    if request.method == 'POST':
        # Form was submitted
        form = CurrencyForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            currency_from = form.cleaned_data['валута_от']
            currency_to = form.cleaned_data['валута_в']
            amount = form.cleaned_data['сума']
            # Get the fix
            currency_from_fix = Currency.objects.get(Наименование=currency_from)
            currency_from_fix = currency_from_fix.Лева / currency_from_fix.За_единица
            currency_to_fix = Currency.objects.get(Наименование=currency_to)
            currency_to_fix = currency_to_fix.Лева / currency_to_fix.За_единица
            # Get the result
            result = (currency_from_fix / currency_to_fix) * amount
            # Return all dependencies along with the calculated result
            return render(request, 'calculator/currency_list.html', {'form': form, 'currencies': currencies,
                                                                     'result': result})
    return render(request, 'calculator/currency_list.html', {'form': form, 'currencies': currencies})
'''


def currencies_list_view(request):
    form = CurrencyForm
    currencies = Currency.objects.all()
    if request.method == 'POST':
        # A calculation was requested
        form = CurrencyForm(data=request.POST)
        if form.is_valid():
            # Form fields passed validation
            currency_from = form.cleaned_data['currency_from']
            currency_to = form.cleaned_data['currency_to']
            amount = form.cleaned_data['amount']
            # Get the fix
            currency_from_fix = Currency.objects.get(Наименование=currency_from)
            currency_from_fix = currency_from_fix.Лева / currency_from_fix.За_единица
            currency_to_fix = Currency.objects.get(Наименование=currency_to)
            currency_to_fix = currency_to_fix.Лева / currency_to_fix.За_единица
            # Get the result
            result = (currency_from_fix / currency_to_fix) * amount
            result = round(result, 2)
            # Proceed
            data = {'success': True, 'result': result}
            return JsonResponse(data)

        else:
            data = {'success': False, 'errors': form.errors.as_json()}
            return JsonResponse(data)

    return render(request, 'calculator/currency_list.html', {'form': form, 'currencies': currencies})