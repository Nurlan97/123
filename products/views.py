# from django.shortcuts import render

from rest_framework import generics
from products import serializers

from products.models import Product

from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StandartPaginationClass(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'owner')
    search_fields = ('title',)



class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = StandartPaginationClass


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class UpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer



