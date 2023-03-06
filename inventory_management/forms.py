from django import forms
from .models import Drink, Sale

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'opening_stock', 'new_stock', 'price', 'damage', 'image',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'damage': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['drink', 'quantity', 'mode_of_payment']
