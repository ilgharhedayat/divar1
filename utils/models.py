from django_jalali.db import models as jmodels
from django.db import models


class BaseModel(models.Model):
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        abstract = True
