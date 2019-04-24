from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.reg, name='regis'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('working', views.working, name='working'),
    path('archive', views.archive, name='archive'),
    path('contacts', views.contacts, name='contacts'),
]
