from django.urls import path
from .views import register_user,all_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('all_user/', all_user, name='all_user'),
]