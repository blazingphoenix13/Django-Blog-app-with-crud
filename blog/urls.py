from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('/delete/<id>/', views.deletelist,name="delete"),
    path('/update/<id>', views.updatelist,name="update"),
]
