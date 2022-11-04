from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projet
from .serializers import ProjetSerializer
from rest_framework import status
import pandas as pd

class ShowListProject(APIView):
    def get(self, request):
        all_projet = Projet.objects.all()
        serializer = ProjetSerializer(all_projet, many=True)
        return Response(serializer.data)

class CreateNewProject(APIView):
    # def post(self, request):
    #     return Projet.objects.create(request)
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
    def get(self, request, file_path, nbline):
        mylist = []
        filename=file_path
        file = pd.read_csv(filename)
        # for f in file:
        #     mylist.append(f)
        #serializer = ProjetSerializer(file)
        return Response(file.head(nbline))