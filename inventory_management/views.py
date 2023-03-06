from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime, timedelta
import datetime

from .models import Drink, Sale
from .forms import DrinkForm, SaleForm



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

    context = {
        'sales': sales,
        'total_sales': total_sales,
        'date_from': date_from,
        'date_to': date_to,
    }

    if request.method == 'POST':
        date_filter = request.POST.get('date_filter')
        if date_filter:
            # Filter sales by selected date
            sales = Sale.objects.filter(date_created__date=date_filter)
            total_sales = sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
            context.update({
                'sales': sales,
                'total_sales': total_sales,
                'date_filter': date_filter
            })

    return render(request, 'sale_report.html', context)

def sale_list(request):
    sales = Sale.objects.all()
    context = {
        'sales': sales
    }
    return render(request, 'sale_list.html', context)


def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            drink = sale.drink
            drink.number_sold += sale.quantity
            drink.total_stock -= sale.quantity
            drink.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sale_create.html', {'form': form})

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





def drink_list(request):
    drinks = Drink.objects.all()
    context = {'drinks': drinks}
    return render(request, 'drink_list.html', context)

def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drink_detail.html', {'drink': drink})

def drink_create(request):
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm()
    return render(request, 'drink_create.html', {'form': form})


def drink_update(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        form = DrinkForm(request.POST, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'drink_update.html', {'form': form})

def drink_delete(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        drink.delete()
        return redirect('drink_list')
    return render(request, 'drink_confirm_delete.html', {'drink': drink})