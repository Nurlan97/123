from rest_framework import serializers
from products.models import Product
from basket.models import Order



class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(pk=attrs['product'])
        except Product.DoesNot.Exist:
            raise serializers.ValidationError('Failed to find the product')
        count = attrs['count']
        data['count'] = count
        data['product'] = product.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Order.objects.create(
            product=product,
            user=user,
            count=data['count'],
        )