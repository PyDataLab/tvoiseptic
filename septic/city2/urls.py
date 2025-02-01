from django.urls import path
from . import views

app_name = 'city2'

urlpatterns = [
    path('', views.city2_content, name='city2_content'),
]