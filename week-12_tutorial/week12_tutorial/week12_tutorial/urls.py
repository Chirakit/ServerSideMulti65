# week12_tutorial/urls.py
from django.contrib import admin
from django.urls import path, include

from bookings.views import Login, Logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("bookings/", include("bookings.urls")),
]
