from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField

from products.models import Product, Recall


class ProductSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    recalls = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def is_liked(self, product):
        user = self.context.get('request').user
        return user.liked.filter(product=product).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recalls_detail'] = RecallSerializer(instance.recalls.all(), many=True).data
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        representation['likes_count'] = instance.likes.count()
        return representation


class RecallSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Recall
        fields = ('id', 'body', 'owner', 'product')