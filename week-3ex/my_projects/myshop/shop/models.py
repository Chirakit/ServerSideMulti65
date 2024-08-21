from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cart(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=False)
    expired_in = models.IntegerField(default=60, null=False)

    def __str__(self):
        return f"{self.create_date} {self.expired_in}"

class CartItem(models.Model):
    cart = models.ForeignKey("shop.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.amount

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    product_category = models.ManyToManyField("shop.ProductCategory")

    def __str__(self):
        return f"{self.name} {self.price}"

class Order(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    order_date = models.DateField(null=False)
    remark = models.TextField(null=True)

    def __str__(self):
        return self.order_date
    
class OrderItem(models.Model):
    order = models.ForeignKey("shop.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.amount
    
class Payment(models.Model):
    order = models.OneToOneField("shop.Order", on_delete=models.CASCADE)
    payment_date = models.DateField(null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)

    def __str__(self):
        return f"{self.price} {self.discount}"

class PaymentItem(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    order_item = models.ForeignKey("shop.OrderItem", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)

    def __str__(self):
        return f"{self.price} {self.discount}"

class PaymentMethod(models.Model):
    QR = "QR"
    CREDIT = "CR"
    PAYMENT_CHOICE = {
        QR: "QR",
        CREDIT: "CREDIT"
    }
    PAYMENT_CHOICE = models.CharField(
        max_length=2,
        choices=PAYMENT_CHOICE
    )
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
