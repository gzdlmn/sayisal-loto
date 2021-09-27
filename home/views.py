from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,reverse
from . models import LuckyCoupon
from datetime import date
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#günlük şanslı kupon otomatik yaratılsın
#şanslı kupon günü bu günden farklı ise yeni kupon oluşturulsun.
def homepage(request):
    today = date.today()
    today_day = date.strftime(today, "%d")
    luckycoupon=LuckyCoupon.objects.latest('id')
    luckycoupon.date = date.strftime(luckycoupon.date, "%d")
    if today_day != luckycoupon.date:
        LuckyCoupon.objects.create()
    return render(request, "home.html", {"luckycoupon":luckycoupon, "today":today})
