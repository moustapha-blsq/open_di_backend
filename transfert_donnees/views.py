from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
# Create your views here.
class Validate_csv(APIView):
    def get(self, request):
        filepath = '/Users/mac/Documents/NewOrgUnit RCI.csv'
        ext = os.path.splitext(filepath)[1]
         # Check if the extension is in the list of valid extensions
        valid_extensions = ['.csv']
        if ext.lower() not in valid_extensions:
            return Response(False)
        return Response(True)
