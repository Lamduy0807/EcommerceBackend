# Generated by Django 3.2.6 on 2021-10-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_lovelist_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('levelOfSave', models.IntegerField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Tag', models.ManyToManyField(blank=True, null=True, to='backend.IngredientsTag')),
            ],
        ),
    ]
