from django.db import models
import datetime

class OrderNumber(models.Model):
    CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
    )
    METHODS = (
        ('1', 'Cash'),
        ('2', 'Card'),
    )
    user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
    address = models.ForeignKey('users.Address', on_delete=models.CASCADE)
    price = models.FloatField()
    order_date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=16, choices=CHOICES, default='Pending')
    payment_method = models.CharField(max_length=1, choices=METHODS)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    order_number = models.ForeignKey('orders.OrderNumber', on_delete=models.CASCADE, related_name='order_number_obj')
    user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    items = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.user)

class Shipment(models.Model):
    value = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.value