from django.urls import path
from . import views

#app_name = 'employee_management'

urlpatterns = [
    # Employee views
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create_employee/', views.create_employee, name='create_employee'),
    # path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/employee_update/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/employee_delete/', views.employee_delete, name='employee_delete'),

    # # Schedule views
    # path('schedules/', views.schedule_list, name='schedule_list'),
    # path('schedules/create_employee_schedule/', views.create_employee_schedule, name='create_employee_schedule'),
    # path('schedules/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    # path('schedules/<int:pk>/edit/', views.schedule_update, name='schedule_update'),
    # path('schedules/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),

    # # Shift views
    # path('shifts/', views.shift_list, name='shift_list'),
    # path('shifts/new/', views.shift_create, name='shift_create'),
    # path('shifts/<int:pk>/', views.shift_detail, name='shift_detail'),
    # path('shifts/<int:pk>/edit/', views.shift_update, name='shift_update'),
    # path('shifts/<int:pk>/delete/', views.shift_delete, name='shift_delete'),

    # # Timesheet views
    # path('timesheets/', views.timesheet_list, name='timesheet_list'),
    # path('timesheets/new/', views.timesheet_create, name='timesheet_create'),
    # path('timesheets/<int:pk>/', views.timesheet_detail, name='timesheet_detail'),
    # path('timesheets/<int:pk>/edit/', views.timesheet_update, name='timesheet_update'),
    # path('timesheets/<int:pk>/delete/', views.timesheet_delete, name='timesheet_delete'),

    # # Report views
    # path('reports/schedules/', views.schedule_report, name='schedule_report'),
    # path('reports/timesheets/', views.timesheet_report, name='timesheet_report'),
]
