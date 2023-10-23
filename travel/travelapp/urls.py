from django.urls import path
from . import views

urlpatterns =[
    path('',views.Hello_world,name='Hello_world'),
    path('demo/',views.demo,name='demo')

]