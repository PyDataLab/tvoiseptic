from django.urls import path
from . import views

app_name = 'city5'

urlpatterns = [
    path('', views.city5_content, name='city5_content'),
]