from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.ProductCreateView.as_view()),
    path('list/', views.ProductListView.as_view()),
    path('detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('list/<int:pk>/like/', views.add_to_liked),
    path('list/<int:pk>/dislike/', views.remove_from_liked),
    path('update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('delete/', views.ProductDeleteView.as_view()),

    path('recalls/', views.RecallListCreateView.as_view()),
    path('recalls/<int:pk>/', views.RecallDetailView.as_view()),
]
