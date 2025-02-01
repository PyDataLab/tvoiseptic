from django.urls import path
from . import views

app_name = 'city6'

urlpatterns = [
    path('', views.city6_content, name='city6_content'),
]