from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from wantads.models import WantAd
from categories.models import Category

# Create your views here.
user = get_user_model()


class PanelView(TemplateView):
    template_name = "config/panel.html"

    def get_context_data(self, **kwargs):
        context_data = super(PanelView, self).get_context_data()
        context_data["user_count"] = user.objects.filter(is_admin=False).count()
        context_data["want_count"] = WantAd.objects.count()
        context_data["category_count"] = Category.objects.count()
        return context_data
