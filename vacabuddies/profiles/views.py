from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Trip
from .utils import get_error_messages

User = get_user_model()


def register(request):
    if request.method == "POST":
        username = request.POST["reg_username"]
        email = request.POST["reg_email"]
        name = request.POST["reg_name"]
        password1 = request.POST["reg_password1"]
        password2 = request.POST["reg_password2"]

        new_user = User(username=username, email=email, last_name=name)
        new_user.set_password(password1)

        try:
            new_user.full_clean()
        except ValidationError as e:
            errors = "\n".join(get_error_messages(e))
            return render(request, "profiles/index.html", {
                "success": False,
                "error": errors
            })

        new_user.save()

        login(request, user)
        return redirect(request, "/")
    else:
        return redirect(request, "/")


def login(request):
    if request.method == "POST":
        username = request.POST["login_username"]
        password = request.POST["login_password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request, "/")
        else:
            return render(
                request,
                "profiles/login.html",
                {
                    "success": False,
                    "error": "Invalid credentials",
                },
            )
    else:
        return render(request, "profiles/index.html")


def home(request):
    if request.user.is_authenticated:
        return render(request, "profiles/home.html")
    else:
        return render(request, "profiles/index.html")


def profile(request):
    if request.user.is_authenticated:
        return render(
            request,
            "profiles/profile_u1.html",
            {
                "user":
                make_user_dict(request.user),
                "planned_trips":
                [make_trip_dict(trip) for trip in user.planned_trips],
                "participated_trips":
                [make_trip_dict(trip) for trip in user.participated_trips],
            },
        )
    else:
        return redirect(request, "/")


def explore(request):
    if request.user.is_authenticated:
        return render(
            request,
            "profiles/profile_u2.html",
            {
                "user": make_user_dict(request.user),
                "trips": [make_trip_dict(trip) for trip in Trip.objects.all()],
            },
        )


def plan(request):
    if request.user.is_authenticated:
        return render(request, "profiles/plantrip.html",
                      {"user": make_user_dict(request.user)})
