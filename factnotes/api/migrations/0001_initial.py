# Generated by Django 5.0.3 on 2024-11-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('bgcolor', models.CharField(default='gray-700', max_length=50)),
                ('archived', models.BooleanField(default=False)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
    ]
