from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dataset/', views.dataset, name='dataset'),
    path('insert/', views.insert, name='insert'),
    path('insert/add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('retrieve/<int:id>', views.retrieve, name='retrieve'),
    path('update/<int:id>', views.update, name='update'),
]