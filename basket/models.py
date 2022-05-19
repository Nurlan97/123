from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='user',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.DO_NOTHING,
    )
    count = models.IntegerField()

