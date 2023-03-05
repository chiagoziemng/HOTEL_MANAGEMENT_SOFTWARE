from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'hire_date', 'hourly_rate']
            # Adding widgets to specify input types for each field
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Adding custom validation to check if the email address is unique
    def clean_email(self):
        email = self.cleaned_data['email']
        existing_employee = Employee.objects.filter(email=email).exclude(id=self.instance.id).first()
        if existing_employee:
            raise forms.ValidationError('This email address is already in use.')
        return email


def validate_time(time_string):
    try:
        datetime.datetime.strptime(time_string, '%H:%M')
    except ValueError:
        raise ValidationError(_('Invalid time format. Enter a valid time in HH:MM format.'))

class EmployeeScheduleForm(forms.ModelForm):
    class Meta:
        model = EmployeeSchedule
        fields = ['employee', 'start_date', 'end_date', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end', 'saturday_start', 'saturday_end', 'sunday_start', 'sunday_end']

        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'monday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'monday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'tuesday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'tuesday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'wednesday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'wednesday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'thursday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'thursday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'friday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'friday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'saturday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'saturday_end': forms.TimeInput(attrs={'class': 'form-control'}),
            'sunday_start': forms.TimeInput(attrs={'class': 'form-control'}),
            'sunday_end': forms.TimeInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            start_time = cleaned_data.get(f"{day}_start")
            end_time = cleaned_data.get(f"{day}_end")
            if start_time and end_time:
                start_time = start_time.strftime('%H:%M')
                end_time = end_time.strftime('%H:%M')
                validate_time(start_time)
                validate_time(end_time)
        return cleaned_data


class EmployeeShiftForm(forms.ModelForm):
    class Meta:
        model = EmployeeShift
        fields = ['start_time', 'end_time', 'date', 'weekday', 'schedule']
        widgets = {
            'schedule': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeShiftForm, self).__init__(*args, **kwargs)
        self.fields['schedule'].queryset = EmployeeSchedule.objects.all()

class EmployeeTimesheetForm(forms.ModelForm):
    date = forms.DateField()
    weekday = forms.ChoiceField(choices=EmployeeShift.WEEKDAYS)
    shift = forms.ModelChoiceField(queryset=EmployeeShift.objects.all())
    start_time = forms.TimeField()
    end_time = forms.TimeField()

    class Meta:
        model = EmployeeTimesheet
        fields = ('date', 'weekday', 'shift', 'start_time', 'end_time')



###################################################################