from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


class Item(models.Model):
    title   = models.CharField(max_length=30)
    slug    = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})


class OrderItem(models.Model):
    SIZES_CHOICES = (
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.SlugField()
    size = models.CharField(max_length=1, choices=SIZES_CHOICES)

    def __str__(self):
        return f'{self.item.title}: {self.size}'


class Customer(models.Model):
    name            = models.CharField(max_length=120)
    email           = models.EmailField()
    phone_number    = PhoneNumberField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer    = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    order_item  = models.ForeignKey(OrderItem, on_delete=models.SET_NULL)

    def __str__(self):
        return self.order_item.item.title