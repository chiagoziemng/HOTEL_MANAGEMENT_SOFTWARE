from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import  post_save
from django.dispatch import receiver

#  Defined Drink Table                      #1

class Drink(models.Model):
    CATEGORY_CHOICES = [
        ('Soft-drink/Non-alcoholic', 'Soft-drink/Non-alcoholic'),
        ('Beer', 'Beer'),
        ('Blended-spirit/Whiskey/Wine', 'Blended-spirit/Whiskey/Wine'),
        ('Others', 'Others')
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Others')
    image = models.ImageField(upload_to='drinks', default='drinks/default.png' ,blank=True, null=True)
    opening_stock = models.IntegerField(default=0)
    new_stock = models.IntegerField(default=0)
    total_stock = models.IntegerField(default=0)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Added a new field called 'total_sales'

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

    def save(self, *args, **kwargs):
        self.total_stock = self.opening_stock + self.new_stock
        self.closing_stock = self.total_stock - self.number_sold - self.damage
        self.amount_sold = self.number_sold * self.price
        super().save(*args, **kwargs)




#  Defined Sale Table                                #2

class Sale(models.Model):
    POS = 'POS'
    TRANSFER = 'TRANSFER'
    CASH = 'CASH'
    DEBT = 'DEBT'
    COMPLIMENTARY = 'COMPLIMENTARY'

    MODE_OF_PAYMENT_CHOICES = [
        ('POS', 'POS'),
        ('TRANSFER', 'TRANSFER'),
        ('CASH', 'CASH'),
        ('DEBT', 'DEBT'),
        ('COMPLIMENTARY', 'COMPLIMENTARY')
    ]
    date_time = models.DateTimeField(auto_now_add=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    debtor_name = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    sale_date = models.DateField()
    
    def save(self, *args, **kwargs):
        self.price = self.drink.price
        self.total_price = self.quantity * self.price
        
        if self.mode_of_payment == 'DEBT':
            if self.debtor_name is None or self.debtor_name == '':
                raise forms.ValidationError('Debtor name is required for debt transactions.')
        elif self.mode_of_payment == 'COMPLIMENTARY':
            if self.customer_name is None or self.customer_name == '':
                raise forms.ValidationError('A name is required for complimentary sales.')
    
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
    
@receiver(post_save, sender=Sale)
def create_debt(sender, instance, created, **kwargs):
    if created and instance.mode_of_payment == 'DEBT':
        Debt.objects.create(
            amount=instance.total_price,
            debtor_name=instance.debtor_name,
        )


#  Defined Debt Table                           #3

class Debt(models.Model):
    STATUS_CHOICES = [
        ('Owing', 'Owing'),
        ('Cleared', 'Cleared'),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    debtor_name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Owing')
    cleared_on = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.debtor_name} - {self.amount} - {self.date} - {self.status}"
    


#  Defined Complimentary Table                 #4

class Complimentary(models.Model):
    name = models.CharField(max_length=50)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.sale.drink.name} - {self.sale.quantity}"
