from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import View
from django.contrib.auth.models import Group



class RegisterFormView(View):
    
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.groups.add(Group.objects.get(name='Персонал'))
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

        return render(request, 'register.html', {'form': form})

    
    
def redirect_view(request):
    if request.user.is_authenticated:
        return redirect('admin:index')
    else:
        return redirect('register')