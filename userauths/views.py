from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL
User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('core:index')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

# gets the login credentials and logs the user in
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey, you are already logged in")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            # Use the correct User model to get the user
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")
            return render(request, "userauths/sign-in.html")  # Return to the sign-in page
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You Are Logged In.")
            return redirect("core:index")
        else:
            messages.warning(request, "Incorrect password. Please try again.")
            
    return render(request, "userauths/sign-in.html")



def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect("userauths:sign-in")