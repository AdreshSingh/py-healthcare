from django.urls import path

from .views import index,dashboard

urlpatterns=[
    path("",index,name="Home"),
    path("dashboard",dashboard,name="Dashboard")
]