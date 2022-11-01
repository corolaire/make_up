
from django.http import JsonResponse
#from django.views.decorators.http import require_http_methods

def saludo(request):
    nombre = request.GET.get("nombre")
    return JsonResponse({"mensaje":f"Saludos {nombre}"})