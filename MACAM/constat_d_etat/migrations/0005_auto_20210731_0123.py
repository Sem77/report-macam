# Generated by Django 3.2 on 2021-07-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0004_auto_20210730_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artgraphique',
            name='revers_inaccessible',
        ),
        migrations.AddField(
            model_name='materiauxsupportartgraphique',
            name='revers_inaccessible',
            field=models.BooleanField(default=True),
        ),
    ]
