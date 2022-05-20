from rest_framework import generics, permissions, status
from products import serializers

from products.models import Product, Recall, Likes
from products.permissions import IsAuthor
# from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view


class StandartPaginationClass(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = StandartPaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('owner',)
    search_fields = ('title',)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


@api_view(['POST'])
def add_to_liked(request, pk):
    product = Product.objects.get(id=pk)
    if request.user.liked.filter(product=product).exists():
        return Response('Вы уже лайкали данный пост', status=status.HTTP_400_BAD_REQUEST)
    Likes.objects.create(product=product, user=request.user)
    return Response('Добавлено в понравившийся', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def remove_from_liked(request, pk):
    product = Product.objects.get(id=pk)
    if not request.user.liked.filter(product=product).exists():
        return Response('Данный пост отсутствует в списке понравившийся',status=status.HTTP_400_BAD_REQUEST)
    request.user.liked.filter(product=product).delete()
    return Response('Убрано из списка понравившийся', status=status.HTTP_204_NO_CONTENT)


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