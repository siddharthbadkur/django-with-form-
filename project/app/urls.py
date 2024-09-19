 
from django.urls import path
from app.views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('gallery/',gallery,name='gallery'),
    path('sss/',sss,name='sss'),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update'),
    path('login/',login,name='login')

]