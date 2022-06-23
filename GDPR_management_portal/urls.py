from django import views
from django.contrib import admin
from django.urls import path
from GDPR_management_portal import views

urlpatterns = [
    path('', views.index,name="index"),
    path('pocresult',views.poc_result,name="poc_result"),
    path('overview',views.overview,name="overview")
    ]