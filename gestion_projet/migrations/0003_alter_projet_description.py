# Generated by Django 3.2.13 on 2023-01-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_projet', '0002_auto_20221026_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]