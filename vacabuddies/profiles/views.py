from django.contrib.auth import authenticate, get_user_model, login
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from .utils import get_error_messages

User = get_user_model()


def auth(request):
    if request.method == "POST":
        if request.POST.get("reg_username"):
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
                return render(
                    request, "profiles/index.html", {"success": False, "error": errors}
                )

            new_user.save()

            login(request, user)
            return redirect(request, "/")
        elif request.POST.get("login_username"):
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
                    {"success": False, "error": "Invalid credentials",},
                )
        else:
            return render(request, "profiles/index.html")
    else:
        return render(request, "profiles/index.html")


def home(request):
    return render(request, "profiles/profile_u2.html")
