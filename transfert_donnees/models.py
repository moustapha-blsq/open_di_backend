from django.db import models

class Source_de_donnees(models.Model):
    id = models.AutoField(primary_key=True)
    nom_source = models.CharField(max_length=100)
    path_reference = models.CharField(max_length=150)
    is_valid = models.CharField(max_length=10)

class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    nom_serveur = models.CharField(max_length=100)
    url_serveur = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=150)
    statut = models.CharField(max_length=20)
    is_valid = models.CharField(max_length=10)