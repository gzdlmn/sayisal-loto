from django.db import models
from random import randint
import random
from django.contrib.auth.models import User

# Create your models here.
#Otomatik kupon doldurma modeli
def random_int():
    liste=range(1,50)
    return random.sample(liste,6)

#otomatik oluşan kupon modeli
class Number(models.Model):
    CHOICE=((None, 'Kuponu göndermek için EVET seçmelisiniz..'), ('evet', 'EVET'), ('hayır', 'HAYIR'))
    choice=models.CharField(choices=CHOICE, null=True, blank=False, max_length=6, verbose_name="Göndermek için Evet seçiniz")
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    numbers=models.CharField(default=random_int, max_length=40, verbose_name='Şanslı Numaralarınız', null=True, blank=False)
    created_date=models.DateTimeField(auto_now_add=True, null=True, blank=False)
    class Meta:
        verbose_name_plural="Otomatik Oyna Sayısal Loto 6/49"
        ordering = ["-created_date"]
    def __str__(self):
        return "{}-{}".format(self.numbers, self.user)
    def save(self, *args, **kwargs):
        if self.choice=='evet':
            super(Number, self).save(*args, **kwargs)



#Kullanıcının kendi doldurduğu kupon modeli
class GuestNumber(models.Model):
    CHOICEYESNO=((None, 'Kuponu göndermek için EVET seçmelisiniz..'), ('evet', 'EVET'), ('hayır', 'HAYIR'))
    choice=models.CharField(choices=CHOICEYESNO, null=True, blank=False, max_length=6)
    guestnumber1 = models.BooleanField(null=True)
    guestnumber2 = models.BooleanField(null=True)
    guestnumber3 = models.BooleanField(null=True)
    guestnumber4 = models.BooleanField(null=True)
    guestnumber5 = models.BooleanField(null=True)
    guestnumber6 = models.BooleanField(null=True)
    guestnumber7 = models.BooleanField(null=True)
    guestnumber8 = models.BooleanField(null=True)
    guestnumber9 = models.BooleanField(null=True)
    guestnumber10 = models.BooleanField(null=True)
    guestnumber11 = models.BooleanField(null=True)
    guestnumber12 = models.BooleanField(null=True)
    guestnumber13 = models.BooleanField(null=True)
    guestnumber14 = models.BooleanField(null=True)
    guestnumber15 = models.BooleanField(null=True)
    guestnumber16 = models.BooleanField(null=True)
    guestnumber17 = models.BooleanField(null=True)
    guestnumber18 = models.BooleanField(null=True)
    guestnumber19 = models.BooleanField(null=True)
    guestnumber20 = models.BooleanField(null=True)
    guestnumber21 = models.BooleanField(null=True)
    guestnumber22 = models.BooleanField(null=True)
    guestnumber23 = models.BooleanField(null=True)
    guestnumber24 = models.BooleanField(null=True)
    guestnumber25 = models.BooleanField(null=True)
    guestnumber26 = models.BooleanField(null=True)
    guestnumber27 = models.BooleanField(null=True)
    guestnumber28 = models.BooleanField(null=True)
    guestnumber29 = models.BooleanField(null=True)
    guestnumber30 = models.BooleanField(null=True)
    guestnumber31 = models.BooleanField(null=True)
    guestnumber32 = models.BooleanField(null=True)
    guestnumber33 = models.BooleanField(null=True)
    guestnumber34 = models.BooleanField(null=True)
    guestnumber35 = models.BooleanField(null=True)
    guestnumber36 = models.BooleanField(null=True)
    guestnumber37 = models.BooleanField(null=True)
    guestnumber38 = models.BooleanField(null=True)
    guestnumber39 = models.BooleanField(null=True)
    guestnumber40 = models.BooleanField(null=True)
    guestnumber41 = models.BooleanField(null=True)
    guestnumber42 = models.BooleanField(null=True)
    guestnumber43 = models.BooleanField(null=True)
    guestnumber44 = models.BooleanField(null=True)
    guestnumber45 = models.BooleanField(null=True)
    guestnumber46 = models.BooleanField(null=True)
    guestnumber47 = models.BooleanField(null=True)
    guestnumber48 = models.BooleanField(null=True)
    guestnumber49 = models.BooleanField(null=True)
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True, null=True, blank=False)
    class Meta:
        verbose_name_plural="Kendin Oyna Sayısal Loto 6/49"
        ordering = ["-created_date"]
    def __str__(self):
        return "{}--{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}" \
               "-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.user,self.guestnumber1,self.guestnumber2,self.guestnumber3,self.guestnumber4,
                                                                   self.guestnumber5,self.guestnumber6,self.guestnumber7,self.guestnumber8,
                                                                   self.guestnumber9,self.guestnumber10,self.guestnumber11,self.guestnumber12,
                                                                   self.guestnumber13,self.guestnumber14,self.guestnumber15,self.guestnumber16,
                                                                   self.guestnumber17,self.guestnumber18,self.guestnumber19,self.guestnumber20,
                                                                   self.guestnumber21,self.guestnumber22,self.guestnumber23,self.guestnumber24,
                                                                   self.guestnumber25,self.guestnumber26,self.guestnumber27,self.guestnumber28,
                                                                   self.guestnumber29,self.guestnumber30,self.guestnumber31,self.guestnumber32,
                                                                   self.guestnumber33,self.guestnumber34,self.guestnumber35,self.guestnumber36,
                                                                   self.guestnumber37,self.guestnumber38,self.guestnumber39,self.guestnumber40,
                                                                   self.guestnumber41,self.guestnumber42,self.guestnumber43,self.guestnumber44,
                                                                   self.guestnumber45,self.guestnumber46,self.guestnumber47,self.guestnumber48,
                                                                   self.guestnumber49)
#guestnumber lar içinde sadece True olan değerler dönsün
    def number_screen(self):
        listenew = []
        if self.guestnumber1 == True:
            listenew.append(1)
        if self.guestnumber2 == True:
            listenew.append(2)
        if self.guestnumber3 == True:
            listenew.append(3)
        if self.guestnumber4 == True:
            listenew.append(4)
        if self.guestnumber5 == True:
            listenew.append(5)
        if self.guestnumber6 == True:
            listenew.append(6)
        if self.guestnumber7 == True:
            listenew.append(7)
        if self.guestnumber8 == True:
            listenew.append(8)
        if self.guestnumber9 == True:
            listenew.append(9)
        if self.guestnumber10 == True:
            listenew.append(10)
        if self.guestnumber11 == True:
            listenew.append(11)
        if self.guestnumber12 == True:
            listenew.append(12)
        if self.guestnumber13 == True:
            listenew.append(13)
        if self.guestnumber14 == True:
            listenew.append(14)
        if self.guestnumber15 == True:
            listenew.append(15)
        if self.guestnumber16 == True:
            listenew.append(16)
        if self.guestnumber17 == True:
            listenew.append(17)
        if self.guestnumber18 == True:
            listenew.append(18)
        if self.guestnumber19 == True:
            listenew.append(19)
        if self.guestnumber20 == True:
            listenew.append(20)
        if self.guestnumber21 == True:
            listenew.append(21)
        if self.guestnumber22 == True:
            listenew.append(22)
        if self.guestnumber23 == True:
            listenew.append(23)
        if self.guestnumber24 == True:
            listenew.append(24)
        if self.guestnumber25 == True:
            listenew.append(25)
        if self.guestnumber26 == True:
            listenew.append(26)
        if self.guestnumber27 == True:
            listenew.append(27)
        if self.guestnumber28 == True:
            listenew.append(28)
        if self.guestnumber29 == True:
            listenew.append(29)
        if self.guestnumber30 == True:
            listenew.append(30)
        if self.guestnumber31 == True:
            listenew.append(31)
        if self.guestnumber32 == True:
            listenew.append(32)
        if self.guestnumber33 == True:
            listenew.append(33)
        if self.guestnumber34 == True:
            listenew.append(34)
        if self.guestnumber35 == True:
            listenew.append(35)
        if self.guestnumber36 == True:
            listenew.append(36)
        if self.guestnumber37 == True:
            listenew.append(37)
        if self.guestnumber38 == True:
            listenew.append(38)
        if self.guestnumber39 == True:
            listenew.append(39)
        if self.guestnumber40 == True:
            listenew.append(40)
        if self.guestnumber41 == True:
            listenew.append(41)
        if self.guestnumber42 == True:
            listenew.append(42)
        if self.guestnumber43 == True:
            listenew.append(43)
        if self.guestnumber44 == True:
            listenew.append(44)
        if self.guestnumber45 == True:
            listenew.append(45)
        if self.guestnumber46 == True:
            listenew.append(46)
        if self.guestnumber47 == True:
            listenew.append(47)
        if self.guestnumber48 == True:
            listenew.append(48)
        if self.guestnumber49 == True:
            listenew.append(49)
        return listenew




#Kullanıcıdan gelen istel-şikayet mesaj modeli
class WishRequest(models.Model):
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    CHOICE=((None,""),("istek","İSTEK"),("şikayet","ŞİKAYET"))
    choice=models.CharField(choices=CHOICE, max_length=7, null=True, blank=False)
    message=models.TextField(null=True, blank=False, verbose_name="Mesajınız")
    class Meta:
        verbose_name_plural="Kullanıcı istek-şikayet formu"
    def __str__(self):
        return "{}---{}".format(self.user, self.choice)