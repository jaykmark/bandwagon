from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

# Register to create a new User account
def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    # Validate if passwords match
    if password == password2:
      # Check is username is already in database
      if User.objects.filter(username = username).exists():
        context = {'error': 'Username is already taken.'}
        return render(request, 'accounts/register.html', context)
      else:
        # Check if email is already in database
        if User.objects.filter(email = email).exists():
          context = {'error': 'Email is already registered.'}
          return render(request, 'accounts/register.html', context)
        else:
          # If everything checks out, create a new User account
          user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password)
          user.save()
          return redirect('login')
    else:
      context = {'error': 'Passwords do not match.'}
      return render(request, 'accounts/register.html', context)
  else:
    # GET request to sent the initial register form
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    # Authenticate username and password
    user = auth.authenticate(username = username, password = password)
    if user is not None:
      auth.login(request, user)
      return redirect('login')
    else:
      context = {'error': 'Invalid Credentials'}
      return render(request, 'accounts/login.html', context)
  else:
    return render(request, 'accounts/login.html')


def logout(request):
  auth.logout(request)
  return redirect('login')