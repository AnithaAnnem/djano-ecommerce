from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username") or request.POST.get("email")
        password = request.POST.get("password")

        # User must exist
        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            messages.error(request, "Invalid username.")
            return HttpResponseRedirect(request.path_info)

        # Authenticate
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")

        messages.error(request, "Invalid credentials")
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/login.html")


def register_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', "") or ""
        last_name = request.POST.get('last_name', "") or ""

        if not username or not email:
            messages.error(request, "Username and email are required.")
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists.')
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists.')
            return HttpResponseRedirect(request.path_info)

        # Create user
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        messages.success(request, 'Account created successfully.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')


def activate_email(request, email_token):
    try:
        profile = Profile.objects.get(email_token=email_token)
        profile.is_email_verified = True
        profile.save()
        return redirect('/')
    except Profile.DoesNotExist:
        return HttpResponse("Invalid Email Activation Link")
