
from django.urls import path
from parseapp import views
urlpatterns = [
    path('', views.index, name='index'),
]