from django.shortcuts import render,redirect,get_object_or_404,Http404
from django.contrib import messages
from . models import Number,GuestNumber,WishRequest
from . forms import NumberForm,WishRequestForm,GuestNumberForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date
from home.models import LuckyCoupon
# Create your views here.

#Kullanıcının otomatik gönderdiği kupon
@login_required(login_url="user:login")
def create_otomatic_number(request):
    form=NumberForm(request.POST or None)
    if form.is_valid():
        number= form.save(commit=False)
        if number.choice=='evet':
            number.user=request.user
            number.save()
            messages.success(request, "Kupun başarıyla gönderildi.Hesabınızdan bakabilirsiniz")
            return redirect("home")
        else:
            messages.warning(request, "Göndermek için EVET'i seçiniz")
            return render(request, "otomatic.html", {"form":form})
    return render(request, "otomatic.html", {"form":form})

#Kullanıcının manuel girdiği kupon
@login_required(login_url="user:login")
def create_manuel_number(request):
    form = GuestNumberForm(request.POST or None)
    if form.is_valid():
        guestnumber = form.save(commit=False)
        if guestnumber.choice == 'evet':
            guestnumber.user = request.user
            listenew = []
            if guestnumber.guestnumber1 == True:
                listenew.append(1)
            if guestnumber.guestnumber2 == True:
                listenew.append(2)
            if guestnumber.guestnumber3 == True:
                listenew.append(3)
            if guestnumber.guestnumber4 == True:
                listenew.append(4)
            if guestnumber.guestnumber5 == True:
                listenew.append(5)
            if guestnumber.guestnumber6 == True:
                listenew.append(6)
            if guestnumber.guestnumber7 == True:
                listenew.append(7)
            if guestnumber.guestnumber8 == True:
                listenew.append(8)
            if guestnumber.guestnumber9 == True:
                listenew.append(9)
            if guestnumber.guestnumber10 == True:
                listenew.append(10)
            if guestnumber.guestnumber11 == True:
                listenew.append(11)
            if guestnumber.guestnumber12 == True:
                listenew.append(12)
            if guestnumber.guestnumber13 == True:
                listenew.append(13)
            if guestnumber.guestnumber14 == True:
                listenew.append(14)
            if guestnumber.guestnumber15 == True:
                listenew.append(15)
            if guestnumber.guestnumber16 == True:
                listenew.append(16)
            if guestnumber.guestnumber17 == True:
                listenew.append(17)
            if guestnumber.guestnumber18 == True:
                listenew.append(18)
            if guestnumber.guestnumber19 == True:
                listenew.append(19)
            if guestnumber.guestnumber20 == True:
                listenew.append(20)
            if guestnumber.guestnumber21 == True:
                listenew.append(21)
            if guestnumber.guestnumber22 == True:
                listenew.append(22)
            if guestnumber.guestnumber23 == True:
                listenew.append(23)
            if guestnumber.guestnumber24 == True:
                listenew.append(24)
            if guestnumber.guestnumber25 == True:
                listenew.append(25)
            if guestnumber.guestnumber26 == True:
                listenew.append(26)
            if guestnumber.guestnumber27 == True:
                listenew.append(27)
            if guestnumber.guestnumber28 == True:
                listenew.append(28)
            if guestnumber.guestnumber29 == True:
                listenew.append(29)
            if guestnumber.guestnumber30 == True:
                listenew.append(30)
            if guestnumber.guestnumber31 == True:
                listenew.append(31)
            if guestnumber.guestnumber32 == True:
                listenew.append(32)
            if guestnumber.guestnumber33 == True:
                listenew.append(33)
            if guestnumber.guestnumber34 == True:
                listenew.append(34)
            if guestnumber.guestnumber35 == True:
                listenew.append(35)
            if guestnumber.guestnumber36 == True:
                listenew.append(36)
            if guestnumber.guestnumber37 == True:
                listenew.append(37)
            if guestnumber.guestnumber38 == True:
                listenew.append(38)
            if guestnumber.guestnumber39 == True:
                listenew.append(39)
            if guestnumber.guestnumber40 == True:
                listenew.append(40)
            if guestnumber.guestnumber41 == True:
                listenew.append(41)
            if guestnumber.guestnumber42 == True:
                listenew.append(42)
            if guestnumber.guestnumber43 == True:
                listenew.append(43)
            if guestnumber.guestnumber44 == True:
                listenew.append(44)
            if guestnumber.guestnumber45 == True:
                listenew.append(45)
            if guestnumber.guestnumber46 == True:
                listenew.append(46)
            if guestnumber.guestnumber47 == True:
                listenew.append(47)
            if guestnumber.guestnumber48 == True:
                listenew.append(48)
            if guestnumber.guestnumber49 == True:
                listenew.append(49)
            if len(listenew) == 6:
                guestnumber.save()
                messages.success(request, "Kupun başarıyla gönderildi.Hesabınızdan bakabilirsiniz")
                return redirect("home")
            else:
                messages.info(request, "Toplamda 6 adet numara seçmeniz gerekmektedir")
        else:
            messages.warning(request, "Göndermek için Onaylıyorum işaretleyiniz")
            return render(request, "manuel.html", {"form": form})
    return render(request, "manuel.html", {"form": form})



#Kullanıcıya ait olan kuponları göster
@login_required(login_url="user:login")
def my_numbers(request):
    today = date.today()
    mynumbers=Number.objects.filter(user=request.user)
    mynumbers_manuel=GuestNumber.objects.filter(user=request.user)
    form = WishRequestForm(request.POST or None)
    if form.is_valid():
        wishrequest = form.save(commit=False)
        wishrequest.user = request.user
        wishrequest.save()
        messages.success(request, "İletiniz başarıyla iletildi.")
        return redirect("home")
    return render(request, "mynumbers.html", {"mynumbers":mynumbers, "mynumbers_manuel":mynumbers_manuel, "form":form, "today":today})