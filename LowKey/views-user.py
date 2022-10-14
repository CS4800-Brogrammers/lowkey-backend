from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

def loginPage(request):
    page = 'login'

    #we don't want users going back to the login page, even manually
    if request.user.is_authenticated:
        pass
        #return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        #does user exist?
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password does not exist")

    context = {'page':page}
    #return render(request, 'base/login_register.html', context)
    pass

def logoutUser(request):
    logout(request)
    #return redirect('home')
    pass

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            #we want to pause commit to check if entered info complies with rules
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            #return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    #return render(request, 'base/login_register.html', {'form':form})
    pass

@login_required(login_url= 'login')
def updateUser(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            #return redirect('user-profile', pk = user.id)

    #return render(request, 'base/update-user.html', {'form': form}) 
    pass

#taken from stackoverflow https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django
@login_required(login_url = 'login')
def deleteUser(request, pk):
    try:
        user = request.user
        user.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User does not exist")    
        #return render(request, 'front.html')

    except Exception as e: 
        pass
        #return render(request, 'front.html',{'err':e.message})

    #return render(request, 'front.html') 
    pass


