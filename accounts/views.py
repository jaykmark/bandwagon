from django.shortcuts import render

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
    password = req.POST['password']
    password2 = req.POST['password2']
      # Validate if passwords match
      if password == password2:
        # Check is username is already in database
        if User.objects.filter(username = username).exists():
          context = {'error': 'Username is already taken.'}
          return render(request, 'register.html', context)
        else:
          # Check if email is already in database
          if User.objects.filter(email = email).exists():
            context = {'error': 'Email is already registered.'}
            return render(request, 'register.html', context)
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
      return render(request, 'register.html', context)
  else:
    # GET request to sent the initial register form
    return render(request, 'register.html')