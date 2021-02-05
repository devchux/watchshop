from django.contrib import admin
from .models import Item, Order, Customer

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display= ['customer', 'item', 'status', 'date_created']

class OrderInline(admin.TabularInline):
    model = Order

class CustomerAdmin(admin.ModelAdmin):
    list_display= ['name',]
    inlines = [
        OrderInline,
    ]




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
