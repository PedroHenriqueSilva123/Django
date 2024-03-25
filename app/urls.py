from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('bulyn', views.bulyn, name='bulyn'),
    path('contato', views.contato, name='contato'),
    path('oquee', views.oquee, name='oquee'),
    path('criadores', views.criadores, name='criadores'),
]