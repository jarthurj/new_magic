from django.urls import path
from .views import Register,Dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("logout/",LogoutView.as_view(),name="logout"),
]