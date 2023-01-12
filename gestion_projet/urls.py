from django.contrib import admin
from django.urls import path
from .views import ShowListProject, CreateNewProject, GetProjetByID, AddSourceCSV, GetSourceHeader

urlpatterns = [
    path('liste_projet/', ShowListProject.as_view()),
    path('create_projet', CreateNewProject.as_view()),
    path('getprojet/<str:pk>', GetProjetByID.as_view()),
    path('testcsv/', AddSourceCSV.as_view()),
    path('csvheader/', GetSourceHeader.as_view())

]