from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EntryForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    entry = Event.objects.all()
    return render(request, 'index.html', {'entry':entry})

def detail(request, entry_id):
    entry = Event.objects.get(id=entry_id)
    return render(request, 'detail.html', {'entry':entry})

def addevent(request):
    form = EntryForm()
    return render(request, 'addevent.html', {'form':form})

def submitevent(request):
    form = EntryForm(request.POST, request.FILES)
    if form.is_valid():
        entry = form.save(commit = False)
        entry.user=request.user
        entry.save()
    return HttpResponseRedirect('/')

def user_profile(request, username):
    user = User.objects.get(username=username)
    entry = Event.objects.filter(user=user)
    return render(request, 'profile.html', {
            'username' : username,
            'entry' : entry}
            )

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u=form.cleaned_data['username']
            p=form.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and/or password were incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
