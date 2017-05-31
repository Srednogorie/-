from django import forms
from .models import Currency


class CurrencyForm(forms.Form):
    валута_от = forms.ModelChoiceField(queryset=Currency.objects.all(), required=True, empty_label="Моля Изберете Валута")
    валута_в = forms.ModelChoiceField(queryset=Currency.objects.all(), required=True, empty_label="Моля Изберете Валута")
    сума = forms.DecimalField(required=True, max_digits=10, decimal_places=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Моля Въведете Сума'}))



