# Generated by Django 3.2.11 on 2022-01-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedarticles',
            name='researchInterest',
            field=models.ManyToManyField(blank=True, to='newsweb.ResearchInterest'),
        ),
    ]
