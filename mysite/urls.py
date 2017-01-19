from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^joke/', views.joke, name='joke'),
    url(r'^trivia/', views.trivia, name='joke'),
    url(r'^response/', views.response, name='joke'),
]
