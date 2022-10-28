from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def saludo(request):
    return JsonResponse({"mensaje":"Saludos"})