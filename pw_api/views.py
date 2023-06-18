from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from  rest_framework.response import Response
from rest_framework import status
from .models import MissingPerson, MostWanted
from .serializers import UserSerializer, MissingPersonSerializer, MostWantedSerializer
import logging

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def list_missing_persons(request):

    try:
        missing_person = MissingPerson.objects.all()
    except missing_person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MissingPersonSerializer(missing_person, many=True)
        context = {
            "Missing": serializer.data
        }
        return JsonResponse(context)
    
    elif request.method == 'POST':
        serializer = MissingPersonSerializer(data=request.data)
        # check if database is valid and save data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def missing_person_details(request, id):
    try:
        missing_person = MissingPerson.objects.get(pk=id)
    except missing_person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MissingPersonSerializer(missing_person)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
@api_view(['GET', 'POST'])
def list_most_wanted(request):

    try:
        mostwanted = MostWanted.objects.all()
    except mostwanted.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MostWantedSerializer(mostwanted, many=True)
        context = {
            "Wanted": serializer.data
        }
        return JsonResponse(context)
    
    elif request.method == 'POST':
        serializer = MostWantedSerializer(data=request.data)
        # check if database is valid and save data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def wanted_person_details(request, id):
    try:
        wanted_person = MostWanted.objects.get(pk=id)
    except wanted_person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MostWantedSerializer(wanted_person)
        return Response(serializer.data, status=status.HTTP_200_OK)


