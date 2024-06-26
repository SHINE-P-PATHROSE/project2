from django.urls import path
from .import views
urlpatterns = [
     path('',views.home,name="home"),
     path('form/',views.form,name='form'),
     path('login/',views.login, name='login'),
     path('logout/',views.logout, name='logout')
]