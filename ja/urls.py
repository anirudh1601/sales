from . import views
from django.urls import path

urlpatterns = [
	path('',views.retrive,name="form"),
    path('data/', views.login,name='login'),
]