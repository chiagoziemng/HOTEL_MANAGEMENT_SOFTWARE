from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
import csv




from .models import Drink
from .forms import DrinkForm
from .utils import render_to_pdf


from django.shortcuts import render
from .models import Drink


@login_required
def drink_list(request):
    category_filter = request.GET.get('category', None)
    stock_filter = request.GET.get('stock', None)
    categories = Drink.CATEGORY_CHOICES

    drinks = Drink.objects.all()
    if category_filter:
        drinks = drinks.filter(category=category_filter)
    if stock_filter:
        # filter by stock, excluding drinks with no stock
        drinks = drinks.exclude(stock=None).filter(Q(stock__lte=10) if stock_filter == 'low' else Q(stock__gt=10))

    paginator = Paginator(drinks, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'export_pdf' in request.GET:
        template = get_template('drink_pdf.html')
        context = {'drinks': drinks}
        html = template.render(context)
        pdf = render_to_pdf('drink_pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "drink_list_%s.pdf" % page_number
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
    elif 'export_csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="drink_list.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Category', 'total_stock'])
        for drink in drinks:
            writer.writerow([drink.name, drink.get_category_display(), drink.total_stock])
        return response

    context = {
        'drinks': drinks,
        'page_obj': page_obj,
        'category_filter': category_filter,
        'stock_filter': stock_filter,
        'categories': categories,
    }
    return render(request, 'drink_list.html', context)
# DRINK INVENTORY

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