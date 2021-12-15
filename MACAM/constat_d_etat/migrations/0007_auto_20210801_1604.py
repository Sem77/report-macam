# Generated by Django 3.2 on 2021-08-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0006_rename_alterations_supportpeinturesurbois_alterations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artgraphique',
            name='numero_inventaire',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='peinturesurbois',
            name='numero_inventaire',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='peinturesurtoile',
            name='numero_inventaire',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]