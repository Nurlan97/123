# from django.contrib.auth import get_user_model
from account.models import CustomUser
from django.db import models
# User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(blank=True, null=True, upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        self.name


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        self.name


class Recall(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='recalls', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='recalls', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.product} -> {self.created_at}'


class Likes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['product', 'user']
