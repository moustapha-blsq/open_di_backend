from django.contrib import admin
from django.urls import path
from .views import ShowListProject, CreateNewProject, GetProjetByID, AddSourceCSV

urlpatterns = [
    path('liste_projet/', ShowListProject.as_view()),
    path('create_projet', CreateNewProject.as_view()),
    path('getprojet/<str:pk>', GetProjetByID.as_view()),
    path('testcsv/<str:filename>/<int:page>', AddSourceCSV.as_view())

]