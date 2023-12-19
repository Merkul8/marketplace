from django.shortcuts import redirect, render
from .forms import CustomerRegisterForm, CustomerLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomerLoginForm()
    return render(request, 'market_auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            # send_test_message.delay(form.cleaned_data['email'])
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = CustomerRegisterForm()
    return render(request, 'market_auth/register.html', {'form': form})
    