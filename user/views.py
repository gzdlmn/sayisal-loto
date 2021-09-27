from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . forms import RegisterForm,LoginForm
from django.contrib import messages

# Create your views here.
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        login(request,user)
        messages.success(request, "Kaydınız başarıyla oluşturuldu")
        return redirect("home")
    return render(request, "register.html", {"form":form})

def loginUser(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=(authenticate(username=username, password=password))
        if user is None:
            messages.info(request, "Kullanıcı bulunamadı...")
            return render(request, "login.html", {"form":form})
        login(request,user)
        messages.success(request, "Başarıyla giriş yaptınız")
        return redirect("home")
    return render(request, "login.html", {"form":form})

def logoutUser(request):
    logout(request)
    messages.success(request, "Hoşçakal Yine bekleriz:)")
    return redirect("home")
