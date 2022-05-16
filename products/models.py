from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(blank=True, null=True, upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()


    def __str__(self):
        self.name


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        self.name

