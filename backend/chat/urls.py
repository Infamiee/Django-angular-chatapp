from django.urls import path
from . import views

urlpatterns = [
    path('token', views.get_chat_token, name='token'),
]