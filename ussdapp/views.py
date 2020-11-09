from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from .models import UssdApplication, Task
from .serializer import UssdSerializer
# from rest_framework import serializer
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes


# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        users = Task.objects.all()
        serializer = UssdSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = UssdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def Welcome(request):
    return HttpResponse("Welcome my app")


# class UssdList(APIView):
#     def get(self, request, **kwargs):
#         ussds = UssdApplication.objects.all()
#         serializers = UssdSerializer(ussds, many=True)
#         data = serializers.serialize('xml', UssdApplication.objects.all())
#         return Response(data)
#
#     def post(self, request, **kwargs):
#         serializers = UssdSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             data = serializers.serialize('xml', UssdApplication.objects.all())
#             # return Response(data)
#
#         return Response(data)


@api_view(['GET'])
def listView(request):
    ussdapp = Task.objects.all()
    serializer = UssdSerializer(ussdapp, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailView(request, pk):
    ussdapp = Task.objects.get(id=pk)
    serializer = UssdSerializer(ussdapp, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createView(request):
    serializer = UssdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
