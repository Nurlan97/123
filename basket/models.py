from django.db import models
from account.models import CustomUser
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING,)
    count = models.IntegerField()