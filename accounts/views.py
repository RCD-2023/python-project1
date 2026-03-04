from django.shortcuts import render, redirect
from django.contrib import messages, auth
# username vine default fara model creat de noi
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views methods here.

# definirea metodei 'register'
def register(request):
    if request.method =='POST':
    # Get form values and put them into variables
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password == password2:
            #Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else: 
                # Check email
                if User.objects.filter(email__iexact=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Daca totul este ok vcreem noul user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now tregistered and can log in')
                    return redirect('login')

                    

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

# definirea metodei 'login'
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

# definirea metodei logout
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')

    return redirect('index')

# definirea metodei dashboard
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)