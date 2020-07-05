from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Activities(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, related_name="activities")


class Likes(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_out")
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_in")


class Bio(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bio")


class Trip(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    description = models.TextField()
