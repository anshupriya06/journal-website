from django.urls import path
from . import views
from .views import index


urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', index, name='index'),
    path('home', index, name='index'),
]
