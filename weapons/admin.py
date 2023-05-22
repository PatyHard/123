from django.contrib import admin
from .models import Weapon


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass
