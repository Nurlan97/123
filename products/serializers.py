from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import  ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'

