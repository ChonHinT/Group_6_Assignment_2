from django import forms
from django.core.validators import RegexValidator

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100,
                                  validators=[RegexValidator('[;&|$<>...]', inverse_match=True)])
