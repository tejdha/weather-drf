from django.shortcuts import render
from django.http import HttpResponse
from .models import book

# Create your views here.
def home(request):
    return HttpResponse('hello user this home page of books app')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Bookserializer

@api_view(['POST'])
def add(request):
    book = Bookserializer(data=request.data)

    if book.is_valid():
        book.save()
        return Response(book.data)
    return Response (book.errors)

@api_view(['GET'])
def books(request):
    data = book.objects.all()

    bok = Bookserializer(data, many=True)
    return Response(bok.data)

# from django.db.models import Q
# @api_view(['GET'])
# def single(request,query):
#     filters = Q (movie__icontains=query) | Q (director__icontains=query)

#     if query.isdigit():
#         filters |= Q(id=int(query))
    
#     data = book.objects.filter(filters)

#     ser = Bookserializer(data,many=True)
#     return Response (ser.data)

@api_view(['PUT'])
def update(request,id):
    dataa = book.objects.get(id=id)
    ser = Bookserializer(dataa, data=request.data)

    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(['DELETE'])
def delete(request,id):

    data = book.objects.get(id=id)

    data.delete()
    return Response("book deleted")
    

from rest_framework.views import APIView

class work(APIView):
    def get(self,request):

        mve = request.GET.get('movie')

        dtr = request.GET.get('director')

        if mve: 
            data = book.objects.filter(movie__icontains=mve)
        elif dtr:
            data = book.objects.filter(director__icontains=dtr)
        else:
            data = book.objects.all()


        ser = Bookserializer(data, many=True)

        return Response(ser.data)

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class wwork(ListCreateAPIView):
    data = book.objects.all()

    serializer_classes = Bookserializer
    

