from django.contrib import admin

# Register your models here.
from .models import Activities, Likes, Trip, Bio


admin.site.register(Activities)
admin.site.register(Likes)
admin.site.register(Trip)
admin.site.register(Bio)
