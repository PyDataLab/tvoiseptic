from django.urls import path
from . import views

app_name = 'city4'

urlpatterns = [
    path('', views.city4_content, name='city4_content'),
]