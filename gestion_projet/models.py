from django.db import models

class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    nom_projet = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_creation = models.CharField(max_length=200)
    statut = models.IntegerField(null=True)
    utilisateur = models.IntegerField(null=True)


# Create your models here.
