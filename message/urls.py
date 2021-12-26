from django.urls import path
from .views import message_list

urlpatterns = [
    path('message/', message_list, name='message_list')
]