

from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:#create relation between model and form
        model=Restaurant
        fields='__all__'


