from django.urls import path
from .views import register_user,all_user,login,logout

urlpatterns = [
    path('register/', register_user, name='register'),
    path('all_user/', all_user, name='all_user'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]