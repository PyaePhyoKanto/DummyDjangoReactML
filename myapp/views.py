from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests


def home_view(request):
    return HttpResponse("Welcome to My Django App!")

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET', 'POST'])
def start_ml_training(request):
    response = requests.post('http://ml:5000/start-training')
    return JsonResponse(response.json())
