from django.shortcuts import render
from weather_api import current_weather
from django.http import JsonResponse
import requests
from datetime import datetime

def weather_view(request):
    if request.method == "GET":
        data = current_weather(59.93, 30.31)  # Результат работы функции current_weather
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
