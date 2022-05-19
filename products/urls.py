from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.CreateView.as_view()),
    path('list/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.DetailAPIView.as_view()),
    path('update/<int:pk>/', views.UpdateView.as_view()),
    path('delete/', views.DeleteView.as_view()),

]


