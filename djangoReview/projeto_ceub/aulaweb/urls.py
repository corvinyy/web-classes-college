from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('produtos', views.list_produtos, name='produtos'),
    path('mostra_detalhes/<int:id>', views.mostra_detalhes, name='mostra_detalhes')
]