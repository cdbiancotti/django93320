from django.urls import path
from home.views import home, listado_de_pinturas, ver_pintura, crear_pintura

urlpatterns = [
    path('', home, name="home"),
    path('pinturas/', listado_de_pinturas, name="listar_pinturas"),
    path('ver_pintura/<int:pk>', ver_pintura, name="ver_pintura"),
    path('crear_pintura/', crear_pintura, name="crear_pintura"),
]
