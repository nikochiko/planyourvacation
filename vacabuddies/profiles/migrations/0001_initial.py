# Generated by Django 3.0.7 on 2020-07-05 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('dates', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participated_trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_out', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_in', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('display', models.CharField(max_length=255, unique=True)),
                ('users', models.ManyToManyField(related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
