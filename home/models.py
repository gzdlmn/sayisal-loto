from django.db import models
import random
# Create your models here.


def lucky():
    list=range(1,50)
    return random.sample(list,6)


class LuckyCoupon(models.Model):
    luckynumbers = models.CharField(default=lucky, max_length=40, verbose_name='Kazanan Kupon', null=True, blank=False)
    date=models.DateField(auto_now_add=True, null=True, blank=False)
    class Meta:
        verbose_name_plural="Kazanan Kupon Numaraları"
    def __str__(self):
        return "{}".format(self.luckynumbers)





