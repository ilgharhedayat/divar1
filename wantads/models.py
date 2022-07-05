from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels
from categories.models import Category
from utils.models import BaseModel
from .utils import WandADBase

user = settings.AUTH_USER_MODEL


class WantAd(BaseModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='want_ad')
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
    data = models.JSONField()
    special = models.BooleanField(default=True)

    objects = jmodels.jManager()

    class Meta:
        ordering = ('special', 'created',)

    def __str__(self):
        return f'{self.user} اگهی {self.title} را در تاریخ {self.created} ثبت کرده '


class Image(BaseModel):
    want = models.ForeignKey(WantAd, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='')

    def clean(self):
        if self.want.images.count() > 20:
            raise ValidationError("حذاکثر عکس برای هر ۀگهی 20 عدد است")


class Note(WandADBase):
    text = models.TextField()


class Bookmark(WandADBase):
    pass


