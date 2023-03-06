# Generated by Django 4.1.7 on 2023-03-06 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0019_remove_drink_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='date',
        ),
        migrations.AddField(
            model_name='drink',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]