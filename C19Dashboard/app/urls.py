from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sg/', views.SentimentGraph.as_view(), name='sg'),
    path('cu/', views.C19Updates.as_view(), name = 'cu'),
    path('health', views.health, name='health'),
    path('404', views.handler404, name='404'),
    path('500', views.handler500, name='500'),
]
