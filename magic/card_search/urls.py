from django.urls import path
from .views import Home,Search


urlpatterns = [
    path('', Home.as_view(),name="home"),
    path('search/',Search.as_view(),name="search")
]
