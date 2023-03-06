from datetime import datetime, timedelta, date
import datetime
from django.db.models.functions import TruncDate
from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

import datetime

from .models import Drink, Sale
from .forms import DrinkForm, SaleForm


@login_required
def sale_report(request):
    # Set default date range to past week
    # Get today's date and use it as the default date for filtering
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    date_from = request.GET.get('date_from', week_ago)
    date_to = request.GET.get('date_to', today)

    # Validate date format
    try:
        date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        date_from = today
    try:
        date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        date_to = today

    # Filter sales by date range
    sales = Sale.objects.filter(date_created__date__range=[date_from, date_to])

    # Calculate total sales for the selected date range
    total_sales = sales.aggregate(Sum('total_price'))['total_price__sum'] or 0

    # Get total sales for each mode of payment
    pos_sales = sales.filter(mode_of_payment='POS').aggregate(Sum('total_price'))['total_price__sum'] or 0
    transfer_sales = sales.filter(mode_of_payment='TRANSFER').aggregate(Sum('total_price'))['total_price__sum'] or 0
    cash_sales = sales.filter(mode_of_payment='CASH').aggregate(Sum('total_price'))['total_price__sum'] or 0
    debt_sales = sales.filter(mode_of_payment='DEBT').aggregate(Sum('total_price'))['total_price__sum'] or 0

    context = {
        'sales': sales,
        'total_sales': total_sales,
        'date_from': date_from,
        'date_to': date_to,
        'pos_sales': pos_sales,
        'transfer_sales': transfer_sales,
        'cash_sales': cash_sales,
        'debt_sales': debt_sales
    }

    if request.method == 'POST':
        date_filter = request.POST.get('date_filter')
        if date_filter:
            # Filter sales by selected date
            sales = Sale.objects.filter(date_created__date=date_filter)
            total_sales = sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
            pos_sales = sales.filter(mode_of_payment='POS').aggregate(Sum('total_price'))['total_price__sum'] or 0
            transfer_sales = sales.filter(mode_of_payment='TRANSFER').aggregate(Sum('total_price'))['total_price__sum'] or 0
            cash_sales = sales.filter(mode_of_payment='CASH').aggregate(Sum('total_price'))['total_price__sum'] or 0
            debt_sales = sales.filter(mode_of_payment='DEBT').aggregate(Sum('total_price'))['total_price__sum'] or 0

            context.update({
                'sales': sales,
                'total_sales': total_sales,
                'pos_sales': pos_sales,
                'transfer_sales': transfer_sales,
                'cash_sales': cash_sales,
                'debt_sales': debt_sales,
                'date_filter': date_filter
            })

    return render(request, 'sale_report.html', context)

@login_required
def sale_list(request):
    sales = Sale.objects.all()
    context = {
        'sales': sales
    }
    return render(request, 'sale_list.html', context)

@login_required
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            if sale.mode_of_payment == 'DEBT':
                sale.name_or_room_number = request.POST.get('name_or_room_number')
            sale.save()
            drink = sale.drink
            drink.number_sold += sale.quantity
            drink.total_stock -= sale.quantity
            drink.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=Sale())
    return render(request, 'sale_create.html', {'form': form})

@login_required
def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            new_sale = form.save()
            drink = new_sale.drink
            drink.number_sold += new_sale.quantity - sale.quantity
            drink.total_stock -= new_sale.quantity - sale.quantity
            drink.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sale_update.html', {'form': form, 'sale': sale})
@login_required
def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        drink = sale.drink
        drink.number_sold -= sale.quantity
        drink.total_stock += sale.quantity
        drink.save()
        sale.delete()
        return redirect('sale_list')
    return render(request, 'sale_confirm_delete.html', {'sale': sale})





# DRINK INVENTORY
@login_required
def drink_list_by_date(request, year, month, day):
    target_date = date(year, month, day)
    drinks = Drink.objects.filter(date_created__date=target_date).order_by('-date_created')
    
    context = {
        'drinks': drinks,
        'target_date': target_date,
    }
    return render(request, 'drink_list_by_date.html', context)

@login_required
def drink_list(request):
    today = datetime.date.today()
    drinks = Drink.objects.filter(date_created__date=today).annotate(date=TruncDate('date_created')).order_by('-date')
    prev_date = today - datetime.timedelta(days=1)
    prev_drinks = Drink.objects.filter(date_created__date=prev_date).annotate(date=TruncDate('date_created')).order_by('-date')
    
    context = {
        'drinks': [],
        'prev_drinks': [],
        'previous_date': prev_date
    }
    
    # Today's stock list
    prev_closing_stock = 0
    for drink in drinks:
        opening_stock = drink.opening_stock
        closing_stock = prev_closing_stock + drink.opening_stock + drink.new_stock - drink.damage - drink.number_sold
        context['drinks'].append({
            'id': drink.id,
            'name': drink.name,
            'image': drink.image,
            'opening_stock': opening_stock,
            'new_stock': drink.new_stock,
            'total_stock': opening_stock + drink.new_stock - drink.damage - drink.number_sold,
            'price': drink.price,
            'number_sold': drink.number_sold,
            'damage': drink.damage,
            'amount_sold': drink.number_sold * drink.price,
            'closing_stock': closing_stock,
            'date': drink.date
        })
        prev_closing_stock = closing_stock
    
    # Previous day's stock list
    prev_closing_stock = 0
    for drink in prev_drinks:
        opening_stock = drink.opening_stock
        closing_stock = prev_closing_stock + drink.opening_stock + drink.new_stock - drink.damage - drink.number_sold
        context['prev_drinks'].append({
            'name': drink.name,
            'image': drink.image,
            'opening_stock': opening_stock,
            'new_stock': drink.new_stock,
            'total_stock': opening_stock + drink.new_stock - drink.damage - drink.number_sold,
            'price': drink.price,
            'number_sold': drink.number_sold,
            'damage': drink.damage,
            'amount_sold': drink.number_sold * drink.price,
            'closing_stock': closing_stock,
            'date': drink.date
        })
        prev_closing_stock = closing_stock
    
    return render(request, 'drink_list.html', context)


@login_required
def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drink_detail.html', {'drink': drink})
@login_required
def drink_create(request):
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            drink = form.save(commit=False)
            if 'image' in request.FILES:
                drink.image = request.FILES['image']
            drink.save()
            return redirect('drink_list')
    else:
        form = DrinkForm()
    return render(request, 'drink_create.html', {'form': form})


@login_required
def drink_update(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'drink_update.html', {'form': form})
@login_required
def drink_delete(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        drink.delete()
        return redirect('drink_list')
    return render(request, 'drink_confirm_delete.html', {'drink': drink})