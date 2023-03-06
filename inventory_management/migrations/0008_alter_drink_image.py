# Generated by Django 4.1.7 on 2023-03-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0007_alter_drink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload a PNG or JPEG image with a maximum size of 1MB', null=True, upload_to='drinks/%Y/%m/%d/', verbose_name='Drink Image'),
        ),
    ]
