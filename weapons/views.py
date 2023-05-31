from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Weapon


class AllWeaponsView(ListView):
    """Предстовление вывода всего оружия"""
    model = Weapon
    template_name = 'index.html'
    paginate_by = 5


class WeaponDetailView(DetailView):
    """Предстовление вывода оружия по id"""
    model = Weapon
    template_name = 'weapons/weapon_detail.html'


class Contact(TemplateView):
    template_name = 'contact.html'


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)