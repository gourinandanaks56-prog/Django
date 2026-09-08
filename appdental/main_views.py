from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser or user.user_type == "admin":
                return redirect("admin_dashboard")

            elif user.user_type == "doctor":
                return redirect("doctor_dashboard")

            elif user.user_type == "patient":
                return redirect("patient_dashboard")

        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "login.html")