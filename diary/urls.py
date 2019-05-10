from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('list/', views.List.as_view(), name='list'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
]
