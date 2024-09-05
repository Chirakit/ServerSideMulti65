from django.urls import path

from myform import views

urlpatterns = [
    path("", views.get_name, name="get_name"),
]