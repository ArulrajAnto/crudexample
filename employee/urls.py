from django.conf.urls import url
from django.contrib import admin   
from employee import views  
urlpatterns = [  
    url(r'^show', views.show, name='show'),
    url(r'^emp', views.emp, name='emp'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^update/(?P<id>[0-9]+)/$', views.update, name='update'),
    url(r'^destroy/(?P<id>[0-9]+)/$', views.destroy, name='destroy'), 
    
]  

