# Generated by Django 5.0 on 2024-01-25 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_companiessorted_country_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chunk',
        ),
    ]