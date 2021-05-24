# Generated by Django 3.2 on 2021-04-29 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='recette',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recette',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]