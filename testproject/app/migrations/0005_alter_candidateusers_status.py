# Generated by Django 5.0 on 2024-01-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_candidateusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateusers',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
