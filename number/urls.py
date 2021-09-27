from django.contrib import admin
from django.urls import path
from. import views

app_name="number"
urlpatterns=[
    path('otomatic/', views.create_otomatic_number, name='otomatic'),
    path('manuel/', views.create_manuel_number, name='manuel'),
    path('mynumbers/', views.my_numbers, name='mynumbers'),
]