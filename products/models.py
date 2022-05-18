from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(blank=True, null=True, upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)



    def __str__(self):
        self.name


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        self.name

