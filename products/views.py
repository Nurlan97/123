# from django.shortcuts import render

from rest_framework import generics, permissions
from products import serializers

from products.permissions import IsAuthor
from products.models import Product, Recall


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class RecallListCreateView(generics.ListCreateAPIView):
    queryset = Recall.objects.all()
    serializer_class = serializers.RecallSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class RecallDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recall.objects.all()
    serializer_class = serializers.RecallSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor, )