from django.http import JsonResponse
from rest_framework.views import APIView
from api.serializers import PersonSerializers
from rest_framework.response import Response
#from django.views.decorators.http import require_http_methods

def saludo(request):
    nombre = request.GET.get("nombre")
    return JsonResponse({"mensaje":f"Saludos {nombre}"})


class Persona(APIView):
    def post(self,request):
        data = PersonSerializers(data=request.data)
        if not data.is_valid():
            return Response({"error":True,"message":"Json mal formado"})
        # return Response({"message":"Mi nombre es Isaias"})
    def get(self,request):
        pass