from django.urls import path
from . import views

#app_name = 'bar'

urlpatterns = [
    # Drink URLs
    path('', views.drink_list, name='drink_list'),
    path('detail/<int:pk>/', views.drink_detail, name='drink_detail'),
    path('create/', views.drink_create, name='drink_create'),
    path('update/<int:pk>/', views.drink_update, name='drink_update'),
    path('delete/<int:pk>/', views.drink_delete, name='drink_delete'),
    path('drink/<int:year>/<int:month>/<int:day>/', views.drink_list_by_date, name='drink_list_by_date'),
    
    # # Sale URLs
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/create/', views.sale_create, name='sale_create'),
    # path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sales/<int:pk>/update/', views.sale_update, name='sale_update'),
    path('sales/<int:pk>/delete/', views.sale_delete, name='sale_delete'),
    
    # # Sale Report URL
    path('sales/sale_report/', views.sale_report, name='sale_report'),
]

