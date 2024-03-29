# Generated by Django 4.1.7 on 2023-03-16 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('debtor_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Owing', 'Owing'), ('Cleared', 'Cleared')], default='Owing', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Soft-drink/Non-alcoholic', 'Soft-drink/Non-alcoholic'), ('Beer', 'Beer'), ('Blended-spirit/Whiskey/Wine', 'Blended-spirit/Whiskey/Wine'), ('Others', 'Others')], default='Others', max_length=100)),
                ('image', models.ImageField(blank=True, default='drinks/default.png', null=True, upload_to='drinks')),
                ('opening_stock', models.IntegerField(default=0)),
                ('new_stock', models.IntegerField(default=0)),
                ('total_stock', models.IntegerField(default=0)),
                ('total_sales', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_sold', models.IntegerField(default=0)),
                ('damage', models.IntegerField(default=0)),
                ('amount_sold', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closing_stock', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Drinks',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mode_of_payment', models.CharField(choices=[('POS', 'POS'), ('TRANSFER', 'TRANSFER'), ('CASH', 'CASH'), ('DEBT', 'DEBT')], max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('debtor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sale_date', models.DateField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.drink')),
            ],
        ),
    ]
