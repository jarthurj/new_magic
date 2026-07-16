from django.urls import path
from .views import Home,Search,Results


urlpatterns = [
    path('', Home.as_view(),name="home"),
    path('search/',Search.as_view(),name="search"),
    path('search/results/',Results.as_view(),name="results")
]
