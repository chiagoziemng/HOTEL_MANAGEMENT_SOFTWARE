from django import forms
from .models import Drink, Sale,  Debt


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['name','category','opening_stock', 'new_stock', 'price', 'damage', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'opening_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'damage': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }



class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_date','drink', 'quantity', 'mode_of_payment', 'debtor_name',]
        widgets = {
            'sale_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'drink': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'mode_of_payment': forms.Select(attrs={'class': 'form-control'}),
            'debtor_name': forms.TextInput(attrs={'class': 'form-control'}),
       
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['debtor_name'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        cleaned_data = super().clean()
        mode_of_payment = cleaned_data.get('mode_of_payment')
        debtor_name = cleaned_data.get('debtor_name')

        if mode_of_payment == 'DEBT' and not debtor_name:
            raise forms.ValidationError('Debtor name is required for debt transactions.')
        



class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['debtor_name', 'amount', 'status']
        widgets = {
            'status': forms.Select(choices=Debt.STATUS_CHOICES)
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError('Amount must be a positive number.')
        return amount




