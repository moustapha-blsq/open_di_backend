from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projet
from .serializers import ProjetSerializer
from rest_framework import status
import csv
import pandas as pd

class ShowListProject(APIView):
    def get(self, request):
        all_projet = Projet.objects.all()
        serializer = ProjetSerializer(all_projet, many=True)
        return Response(serializer.data)

class CreateNewProject(APIView):
    def post(self, request):
        serializer = ProjetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetProjetByID(APIView):
    def get(self, request, pk):
        #id = request.query_params["id"]
        #print(id)
        projet = Projet.objects.get(id=pk)
        serializer = ProjetSerializer(projet)
        return Response(serializer.data)

class AddSourceCSV(APIView):
    def get(self, request):
        mylist = []
        #file_name = 'gestion_projet/instances.csv'
        file_header = []
        with open('gestion_projet/instances.csv') as datas:
            file_data = csv.reader(datas, delimiter=',')
            #file_header = next(file_data)
            for row in file_data:
                mylist.append(row)
       # serializer = ProjetSerializer(mylist)

        return Response(mylist)

class GetSourceHeader(APIView):
    def get(self, request):
        mylist = []
        #file_name = 'gestion_projet/instances.csv'
        file_header = []
        with open('gestion_projet/instances.csv') as datas:
            file_data = csv.reader(datas, delimiter=',')
            file_header = next(file_data)
            # for row in file_data:
            #     mylist.append(row)
       # serializer = ProjetSerializer(mylist)
        return Response(file_header)