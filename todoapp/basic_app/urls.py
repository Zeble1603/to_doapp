"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = 'basic_app'

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.TaskListView.as_view(),name='home'),
    path('new/',views.TaskCreateView.as_view(),name='create'),
    path('delete/<pk>',views.TaskDeleteView.as_view(),name='delete'),
    path('update/<pk>',views.TaskUpdateView.as_view(),name='update'),
]