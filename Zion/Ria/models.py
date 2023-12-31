from django.db import models
from django.contrib.auth.models import User
import uuid


PRODUCT_STATUS = (
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable')
)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Ria_images/', blank=True, null=True)
    other_image = models.ImageField(upload_to='Ria_images/', blank=True, null=True)
    status = models.CharField(max_length=100, choices=PRODUCT_STATUS)

    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name