from django.db import models
from back_office.products.models import Product
from back_office.products.models import Discount as order_discount
from back_office.customers.models import UserDetail
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('canceled', 'Canceled'),
]


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True, editable=False)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_products = models.ManyToManyField(Product, through='OrderItem')
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    discounts = models.ForeignKey(
        order_discount, on_delete=models.SET_NULL, null=True, blank=True)
    order_user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    checkout_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    status = models.CharField(null=True, blank=True,
                              max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.order_number} - {self.status}"

    def update_total_cost(self):
        total = sum(
            [order_item.item_price for order_item in self.order_items.all()])
        self.total_cost = total
        self.save()


class OrderNumberCounter(models.Model):
    counter = models.IntegerField(default=0)


@receiver(post_save, sender=Order)
def update_order_number(sender, instance, created, **kwargs):
    if created:
        counter, _ = OrderNumberCounter.objects.get_or_create()
        counter.counter += 1
        counter.save()

        instance.order_number = f"Order-{counter.counter:03d}"
        instance.save(update_fields=['order_number'])


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"

    def save(self, *args, **kwargs):
        self.item_price = self.product.price * \
            self.quantity
        super().save(*args, **kwargs)


@receiver(post_save, sender=OrderItem)
def update_order_total_cost(sender, instance, **kwargs):
    instance.order.update_total_cost()
