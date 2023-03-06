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
        fields = ['drink', 'quantity', 'mode_of_payment', 'name_or_room_number']
        widgets = {
            'drink': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'mode_of_payment': forms.Select(attrs={'class': 'form-control'}),
            'name_or_room_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_or_room_number'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        cleaned_data = super().clean()
        mode_of_payment = cleaned_data.get('mode_of_payment')
        name_or_room_number = cleaned_data.get('name_or_room_number')

        if mode_of_payment == 'DEBT' and not name_or_room_number:
            raise forms.ValidationError('Name or room number is required for debt transactions.')



