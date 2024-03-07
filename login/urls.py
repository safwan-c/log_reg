from django.urls import path
from . import views
from django.views. decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', views.login, name='login'),
    path('reg/', views.reg, name='reg'),
    path('login/log',csrf_exempt (views.log), name='log'),
    path('reg/regi', csrf_exempt (views.regi), name='regi'),
    path('dist', csrf_exempt (views.dist), name='dist'),
    
]
