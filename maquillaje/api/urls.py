from django.urls import path
from . import views


urlpatterns = [
    path("saludo/",views.saludo),
    path("create/person/",views.Persona.as_view())
]