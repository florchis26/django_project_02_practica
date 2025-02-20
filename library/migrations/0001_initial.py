# Generated by Django 5.1.6 on 2025-02-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('year', models.DateField()),
            ],
        ),
    ]
