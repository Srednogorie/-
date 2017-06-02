from django import forms
from .models import Currency


class CurrencyForm(forms.Form):
    currency_from = forms.ModelChoiceField(label='', queryset=Currency.objects.all(),
                                           required=True, empty_label="Моля Изберете Валута")
    currency_to = forms.ModelChoiceField(label='', queryset=Currency.objects.all(),
                                         required=True, empty_label="Моля Изберете Валута")
    amount = forms.DecimalField(label='', required=True, max_digits=10, decimal_places=2,
                                widget=forms.TextInput(attrs={'placeholder': 'Моля Въведете Сума'}))
