from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='drinks', default='drinks/default.png' ,blank=True, null=True)
    opening_stock = models.IntegerField(default=0)
    new_stock = models.IntegerField(default=0)
    total_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_sold = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    amount_sold = models.DecimalField(max_digits=10, decimal_places=2)
    closing_stock = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Drinks'

@receiver(pre_save, sender=Drink)
def update_drink_stock(sender, instance, **kwargs):
    instance.total_stock = instance.opening_stock + instance.new_stock - instance.damage - instance.number_sold
    instance.amount_sold = instance.number_sold * instance.price
    instance.closing_stock = instance.total_stock - instance.number_sold



class Sale(models.Model):
    MODE_OF_PAYMENT_CHOICES = [
        ('POS', 'POS'),
        ('TRANSFER', 'TRANSFER'),
        ('CASH', 'CASH'),
        ('DEBT', 'DEBT')
    ]
    
    date_time = models.DateTimeField(auto_now_add=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    name_or_room_number = models.CharField(max_length=50, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.price = self.drink.price
        self.total_price = self.quantity * self.price
        
        if self.mode_of_payment == 'DEBT':
            if self.name_or_room_number is None or self.name_or_room_number == '':
                raise forms.ValidationError('Name or room number is required for debt transactions.')
            
        total_stock = self.drink.opening_stock + self.drink.new_stock - self.drink.damage - self.drink.number_sold
        if total_stock < self.quantity:
            raise ValidationError('Insufficient stock for this drink.')
        
        
        super().save(*args, **kwargs)
    def clean(self):
        # Check if the drink has enough stock to fulfill the sale
        if self.quantity > self.drink.total_stock:
            raise ValidationError('Insufficient stock for this drink.')

    
    def __str__(self):
        return f"{self.drink.name} - {self.quantity} - {self.total_price}"





# class Sale(models.Model):
#     MODE_OF_PAYMENT_CHOICES = [
#         ('POS', 'POS'),
#         ('TRANSFER', 'TRANSFER'),
#         ('CASH', 'CASH'),
#         ('DEBT', 'DEBT')
#     ]
    
#     date_time = models.DateTimeField(auto_now_add=True)
#     drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     def save(self, *args, **kwargs):
#         self.price = self.drink.price
#         self.total_price = self.quantity * self.price
#         super().save(*args, **kwargs)

    
#     def __str__(self):
#         return f"{self.drink.name} - {self.quantity} - {self.total_price}"
