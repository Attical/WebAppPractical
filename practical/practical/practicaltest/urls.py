from django.urls import path
from practicaltest import views

app_name = 'practical'

urlpatterns = [
    path('', views.index, name='index'),
]