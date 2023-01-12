from django.db import models

class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_role = models.CharField(max_length=100)

class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    nom_groupe = models.CharField(max_length=100)

class UserGroupRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey('UserRole', on_delete=models.CASCADE)
    groupe = models.ForeignKey('UserGroup', on_delete=models.CASCADE)