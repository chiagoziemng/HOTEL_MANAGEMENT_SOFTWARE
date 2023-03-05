from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    hire_date = models.DateField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class EmployeeSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monday_start = models.TimeField()
    monday_end = models.TimeField()
    tuesday_start = models.TimeField()
    tuesday_end = models.TimeField()
    wednesday_start = models.TimeField()
    wednesday_end = models.TimeField()
    thursday_start = models.TimeField()
    thursday_end = models.TimeField()
    friday_start = models.TimeField()
    friday_end = models.TimeField()
    saturday_start = models.TimeField()
    saturday_end = models.TimeField()
    sunday_start = models.TimeField()
    sunday_end = models.TimeField()

    def __str__(self):
        return f"{self.employee} Schedule"
    

class EmployeeShift(models.Model):
    WEEKDAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    weekday = models.IntegerField(choices=WEEKDAYS)
    schedule = models.ForeignKey('EmployeeSchedule', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['date', 'start_time']

    def __str__(self):
        return f'{self.schedule.employee}: {self.date} {self.start_time}-{self.end_time}'
    
class EmployeeTimesheet(models.Model):
    date = models.DateField()
    day_of_week = models.CharField(max_length=9, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    shift = models.ForeignKey(EmployeeShift, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.shift.employee.name} - {self.start_time} to {self.end_time}"