from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('recuperar-senha/', views.recuperar_senha_view, name='recuperar_senha'),
    path('nova-senha/', views.nova_senha_view, name='nova_senha'),
    path('bem-vindo/', views.bem_vindo_view, name='bem_vindo'),
]