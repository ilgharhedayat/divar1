from django.contrib import admin
from .models import WantAd


# Register your models here.
@admin.register(WantAd)
class WantAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'created',)
