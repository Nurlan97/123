from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.ProductCreateView.as_view()),
    path('list/', views.ProductListView.as_view()),
    path('view/<int:pk>/', views.ProductDetailView.as_view()),
    path('update/', views.ProductUpdateView.as_view()),
    path('delete/', views.ProductDeleteView.as_view()),

    path('recalls/', views.RecallListCreateView.as_view()),
    path('recalls/<int:pk>/', views.RecallDetailView.as_view()),
]

