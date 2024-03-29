# Generated by Django 3.2.13 on 2023-01-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_serveur', models.CharField(max_length=100)),
                ('url_serveur', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=150)),
                ('statut', models.CharField(max_length=20)),
                ('is_valid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Source_de_donnees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_source', models.CharField(max_length=100)),
                ('path_reference', models.CharField(max_length=150)),
                ('is_valid', models.CharField(max_length=10)),
            ],
        ),
    ]
