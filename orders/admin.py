from django.contrib import admin
from orders.models import Order, OrderNumber, Shipment


class OrderAdminConfig(admin.ModelAdmin):
    model = Order
    search_fields = ('order_number', 'product', 'user')
    list_filter = ('order_number', 'product', 'user')
    list_display = ('order_number', 'product', 'user', 'items', 'price')
    fieldsets = (
        ('Order Information', {'fields': ('order_number', 'user', 'product', 'items', 'price',)}),
    )

class OrderInline(admin.StackedInline):
    model = Order
    extra = 0

class OrderNumberAdminConfig(admin.ModelAdmin):
    model = OrderNumber
    search_fields = ('id', 'user', 'status')
    list_filter = ('id', 'user', 'order_date', 'status', 'payment_method')
    list_display = ('id', 'user', 'order_date', 'price', 'status', 'payment_method')
    fieldsets = (
        ('OrderNumber Information',
         {'fields': ('user', 'address', 'order_date', 'price', 'status', 'payment_method')}),
    )
    inlines = [
        OrderInline,
    ]

class ShipmentAdminConfig(admin.ModelAdmin):
    model = Shipment
    search_fields = ('value',)
    list_filter = ('value',)
    list_display = ('value',)
    fieldsets = (
        ('Shipment Information', {'fields': ('value',)}),
    )





admin.site.register(Order, OrderAdminConfig)
admin.site.register(OrderNumber, OrderNumberAdminConfig)
admin.site.register(Shipment, ShipmentAdminConfig)