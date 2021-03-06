from django.urls import path
from . import views

urlpatterns = [
    path('/cadastro', views.cadastro, name="cadastro.html"),
    path('', views.index, name="index.html"),
    path('/produtos', views.produtos, name="produtos.html"),
    path('/menu', views.menu, name="menu.html"),
    path('/login', views.login, name="login.html"),
]