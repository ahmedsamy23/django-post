from django.shortcuts import render
from .models import About
from post.models import Category
from django.views.generic import ListView
# Create your views here.


class AboutView(ListView):
    model = About
    template_name = 'about_us/about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context