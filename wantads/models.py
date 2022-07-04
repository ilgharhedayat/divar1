from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.postgres.fields import JSONField
from categories.models import Category

user = settings.AUTH_USER_MODEL


class WantAd(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    description = models.TextField()
    active_chat = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='want_ad')
    city = models.CharField(max_length=125)
    zone = models.CharField(max_length=125)
    confirmed = models.BooleanField()
    lat = models.DecimalField(max_digits=5, decimal_places=2, )
    long = models.DecimalField(max_digits=5, decimal_places=2, )
    show_phone = models.BooleanField()
    data = JSONField()
