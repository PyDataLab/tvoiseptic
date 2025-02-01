from django.urls import path
from . import views

app_name = 'city3'

urlpatterns = [
    path('', views.city3_content, name='city3_content'),
]