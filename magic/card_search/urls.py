from django.urls import path
from .views import Home,Search,Results,CardDetailView
from django.contrib import admin

urlpatterns = [
    path('', Home.as_view(),name="home"),
    path('search/',Search.as_view(),name="search"),
    path('search/results/',Results.as_view(),name="results"),
    path("card/<int:pk>/", CardDetailView.as_view(), name="card"),
]

