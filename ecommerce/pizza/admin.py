from django.contrib import admin

from .models import Customer, Item, OrderItem, Order

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)