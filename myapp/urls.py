from django.urls import include, path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
]