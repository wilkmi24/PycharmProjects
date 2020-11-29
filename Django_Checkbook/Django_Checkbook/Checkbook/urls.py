from django.contrib import admin
from django.urls import path, include


urlpattersn = [
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('balance/', views.balance, name='balance',
    path('transaction/', views.transaction, name='transaction'),
]