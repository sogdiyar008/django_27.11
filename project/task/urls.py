from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), #http://127.0.0.1:8000/app/user/Tom/23
    path('error',error, name='error'),
    path('user/<str:login>/<str:directory>/<int:number_post>', user, name='user'),
    path('user/<str:login>/<str:directory>', user, name='user'),
    path('user/<str:login>', user, name='user'),
    path('user', user, name='user'),

]