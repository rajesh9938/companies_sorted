# Generated by Django 5.0 on 2024-01-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_chunk_data_chunk_doom_chunk_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companiessorted',
            name='userid',
        ),
        migrations.AddField(
            model_name='companiessorted',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]