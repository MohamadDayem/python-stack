from django.urls import path
from . import views
urlpatterns =[
    path('', views.root),
    path('blogs', views.index),
    path('blogs/news', views.news),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show)
]