from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        #p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            #p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=request.user)
        #p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        #'p_form': p_form
    }
    return render(request, 'blog/users/profile.html', context)
