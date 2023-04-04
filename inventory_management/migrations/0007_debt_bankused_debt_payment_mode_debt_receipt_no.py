# Generated by Django 4.1.7 on 2023-03-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_remove_drink_closing_stock_remove_drink_damage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='bankused',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='debt',
            name='payment_mode',
            field=models.CharField(choices=[('POS', 'POS'), ('TRANSFER', 'TRANSFER'), ('CASH', 'CASH')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debt',
            name='receipt_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]