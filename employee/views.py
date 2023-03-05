from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Sum
from django.forms import formset_factory  #schedules, shifts, and timesheets
from django.contrib import messages


# EMPLOYEE VIEWS

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('employee_list')



# SCHEDULE VIEWS
def schedule_list(request):
    schedules = EmployeeSchedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def create_employee_schedule(request):
    form = EmployeeScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_schedule_list')
    context = {
        'form': form
    }
    return render(request, 'create_employee_schedule.html', context)


def schedule_edit(request, pk):
    schedule = get_object_or_404(EmployeeSchedule, pk=pk)
    if request.method == 'POST':
        form = EmployeeScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.save()
            return redirect('schedule_list')
    else:
        form = EmployeeScheduleForm(instance=schedule)
    return render(request, 'schedule_edit.html', {'form': form})

def schedule_delete(request, pk):
    schedule = get_object_or_404(EmployeeSchedule, pk=pk)
    schedule.delete()
    return redirect('schedule_list')




################

def shift_list(request):
    shifts = EmployeeShift.objects.all()
    return render(request, 'shift_list.html', {'shifts': shifts})

def create_employee_shift(request):
    schedules = EmployeeSchedule.objects.all()
    if request.method == 'POST':
        form = EmployeeShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.schedule = form.cleaned_data['schedule']
            shift.save()
            return redirect('shift_detail', pk=shift.pk)
    else:
        form = EmployeeShiftForm()
    return render(request, 'create_employee_shift.html', {'form': form, 'schedules': schedules})


def shift_edit(request, pk):
    shift = get_object_or_404(EmployeeShift, pk=pk)
    if request.method == "POST":
        form = EmployeeShiftForm(request.POST, instance=shift)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.save()
            return redirect('shift_list')
    else:
        form = EmployeeShiftForm(instance=shift)
    return render(request, 'shift_edit.html', {'form': form})

def shift_delete(request, pk):
    shift = get_object_or_404(EmployeeShift, pk=pk)
    shift.delete()
    return redirect('shift_list')



##########################
def timesheet_list(request):
    timesheets = EmployeeTimesheet.objects.all()
    return render(request, 'timesheet_list.html', {'timesheets': timesheets})


def create_employee_timesheet(request):
    if request.method == 'POST':
        form = EmployeeTimesheetForm(request.POST)
        if form.is_valid():
            timesheet = form.save()
            return redirect('employee_timesheet_detail', pk=timesheet.pk)
    else:
        form = EmployeeTimesheetForm()
    return render(request, 'create_employee_timesheet.html', {'form': form})


def timesheet_edit(request, pk):
    timesheet = get_object_or_404(EmployeeTimesheet, pk=pk)
    if request.method == "POST":
        form = EmployeeTimesheetForm(request.POST, instance=timesheet)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.save()
            return redirect('timesheet_list')
    else:
        form = EmployeeTimesheetForm(instance=timesheet)
    return render(request, 'timesheet_edit.html', {'form': form})


def timesheet_delete(request, pk):
    timesheet = get_object_or_404(EmployeeTimesheet, pk=pk)
    timesheet.delete()
    return redirect('timesheet_list')




#Employee Schedule Report:Employee Hours Worked Report:Employee Schedule and Hours Worked Report:
def employee_schedule_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        schedules = EmployeeSchedule.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
        context = {'schedules': schedules, 'start_date': start_date, 'end_date': end_date}
        return render(request, 'employee_schedule_report.html', context)
    else:
        return render(request, 'employee_schedule_report_form.html')
    

def employee_hours_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        employees = Employee.objects.all()
        data = []
        for employee in employees:
            shifts = EmployeeShift.objects.filter(schedule__employee=employee, date__gte=start_date, date__lte=end_date)
            timesheets = EmployeeTimesheet.objects.filter(shift__in=shifts)
            hours_worked = timesheets.aggregate(Sum('hours_worked'))['hours_worked__sum']
            data.append({'employee': employee, 'hours_worked': hours_worked})
        context = {'data': data, 'start_date': start_date, 'end_date': end_date}
        return render(request, 'employee_hours_report.html', context)
    else:
        return render(request, 'employee_hours_report_form.html')
    
def employee_schedule_hours_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        employees = Employee.objects.all()
        data = []
        for employee in employees:
            schedule = EmployeeSchedule.objects.filter(employee=employee, start_date__gte=start_date, end_date__lte=end_date).first()
            shifts = EmployeeShift.objects.filter(schedule=schedule, date__gte=start_date, date__lte=end_date)
            timesheets = EmployeeTimesheet.objects.filter(shift__in=shifts)
            hours_worked = timesheets.aggregate(Sum('hours_worked'))['hours_worked__sum']
            data.append({'employee': employee, 'schedule': schedule, 'hours_worked': hours_worked})
        context = {'data': data, 'start_date': start_date, 'end_date': end_date}
        return render(request, 'employee_schedule_hours_report.html', context)
    else:
        return render(request, 'employee_schedule_hours_report_form.html')



