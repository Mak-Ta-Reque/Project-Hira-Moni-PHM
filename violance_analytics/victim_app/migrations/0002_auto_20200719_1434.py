# Generated by Django 3.0.7 on 2020-07-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victim_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='victimapplication',
            name='age_criminal',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='victimapplication',
            name='age_victim',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
