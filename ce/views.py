from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    GenericAPIView, 
    RetrieveUpdateAPIView, 
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)

from .tasks import celery_testing_func
# Create your views here.
def TestView(request):
    
    celery_testing_func.delay()    
    return HttpResponse("You request has received, check console now!")