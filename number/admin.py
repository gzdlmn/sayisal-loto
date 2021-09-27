from django.contrib import admin
from . models import Number,GuestNumber,WishRequest

# Register your models here.

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ["user", "numbers", "choice"]

admin.site.register(GuestNumber)

@admin.register(WishRequest)
class WishRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "choice", "message"]